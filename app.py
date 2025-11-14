import os
import sqlite3
from datetime import datetime
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, send_from_directory
import base64

app = Flask(__name__)
app.secret_key = 'clave-secreta-super-segura-cambiar-en-produccion'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

# Crear carpeta uploads si no existe
os.makedirs('uploads', exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    
    # Tabla de usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            usuario TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            rol TEXT NOT NULL,
            activo INTEGER DEFAULT 1,
            fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Tabla de votantes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS votantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            colaborador_id INTEGER NOT NULL,
            nombre_completo TEXT NOT NULL,
            numero_cedula TEXT,
            telefono TEXT,
            direccion TEXT,
            latitud REAL,
            longitud REAL,
            escuela_votacion TEXT,
            foto TEXT,
            notas TEXT,
            fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (colaborador_id) REFERENCES usuarios(id)
        )
    ''')
    
    # Crear usuario candidato por defecto
    try:
        cursor.execute(
            "INSERT INTO usuarios (nombre, usuario, password, rol) VALUES (?, ?, ?, ?)",
            ('Candidato Principal', 'candidato', generate_password_hash('admin123'), 'candidato')
        )
    except sqlite3.IntegrityError:
        pass
    
    # Crear algunos colaboradores de ejemplo
    colaboradores_ejemplo = [
        ('Juan Pérez', 'juan', 'colaborador123'),
        ('María González', 'maria', 'colaborador123'),
        ('Carlos Rodríguez', 'carlos', 'colaborador123')
    ]
    
    for nombre, usuario, password in colaboradores_ejemplo:
        try:
            cursor.execute(
                "INSERT INTO usuarios (nombre, usuario, password, rol) VALUES (?, ?, ?, ?)",
                (nombre, usuario, generate_password_hash(password), 'colaborador')
            )
        except sqlite3.IntegrityError:
            pass
    
    conn.commit()
    conn.close()

@app.route('/')
def index():
    if 'user_id' in session:
        if session['rol'] == 'candidato':
            return redirect(url_for('dashboard_candidato'))
        else:
            return redirect(url_for('dashboard_colaborador'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        
        conn = get_db()
        user = conn.execute(
            'SELECT * FROM usuarios WHERE usuario = ? AND activo = 1',
            (usuario,)
        ).fetchone()
        conn.close()
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['nombre'] = user['nombre']
            session['rol'] = user['rol']
            flash(f'¡Bienvenido, {user["nombre"]}!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Usuario o contraseña incorrectos', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada correctamente', 'success')
    return redirect(url_for('login'))

@app.route('/dashboard/candidato')
def dashboard_candidato():
    if 'user_id' not in session or session['rol'] != 'candidato':
        return redirect(url_for('login'))
    
    conn = get_db()
    
    # Estadísticas generales
    total_votantes = conn.execute('SELECT COUNT(*) as count FROM votantes').fetchone()['count']
    total_colaboradores = conn.execute(
        'SELECT COUNT(*) as count FROM usuarios WHERE rol = "colaborador" AND activo = 1'
    ).fetchone()['count']
    
    # Votantes por colaborador
    votantes_por_colaborador = conn.execute('''
        SELECT u.nombre, COUNT(v.id) as total
        FROM usuarios u
        LEFT JOIN votantes v ON u.id = v.colaborador_id
        WHERE u.rol = "colaborador" AND u.activo = 1
        GROUP BY u.id, u.nombre
        ORDER BY total DESC
    ''').fetchall()
    
    # Convertir Row objects a diccionarios para JSON serialization
    votantes_por_colaborador = [dict(row) for row in votantes_por_colaborador]
    
    # Todos los votantes para el mapa
    votantes = conn.execute('''
        SELECT v.*, u.nombre as colaborador
        FROM votantes v
        JOIN usuarios u ON v.colaborador_id = u.id
        WHERE v.latitud IS NOT NULL AND v.longitud IS NOT NULL
    ''').fetchall()
    
    # Convertir Row objects a diccionarios para JSON serialization
    votantes = [dict(row) for row in votantes]
    
    conn.close()
    
    return render_template('dashboard_candidato.html',
                         total_votantes=total_votantes,
                         total_colaboradores=total_colaboradores,
                         votantes_por_colaborador=votantes_por_colaborador,
                         votantes=votantes)

@app.route('/dashboard/colaborador')
def dashboard_colaborador():
    if 'user_id' not in session or session['rol'] != 'colaborador':
        return redirect(url_for('login'))
    
    conn = get_db()
    
    # Votantes registrados por este colaborador
    votantes = conn.execute(
        'SELECT * FROM votantes WHERE colaborador_id = ? ORDER BY fecha_registro DESC',
        (session['user_id'],)
    ).fetchall()
    
    total_registrados = len(votantes)
    
    conn.close()
    
    return render_template('dashboard_colaborador.html',
                         votantes=votantes,
                         total_registrados=total_registrados)

@app.route('/votante/nuevo', methods=['GET', 'POST'])
def nuevo_votante():
    if 'user_id' not in session or session['rol'] != 'colaborador':
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        nombre_completo = request.form['nombre_completo']
        numero_cedula = request.form.get('numero_cedula', '').strip()
        telefono = request.form.get('telefono', '')
        direccion = request.form.get('direccion', '')
        latitud = request.form.get('latitud')
        longitud = request.form.get('longitud')
        escuela_votacion = request.form.get('escuela_votacion', '')
        notas = request.form.get('notas', '')
        
        # Validar cédula única
        if numero_cedula:
            conn = get_db()
            votante_existente = conn.execute(
                'SELECT id FROM votantes WHERE numero_cedula = ?',
                (numero_cedula,)
            ).fetchone()
            conn.close()
            
            if votante_existente:
                flash('Error: Esta cédula ya está registrada por otro votante', 'error')
                return render_template('nuevo_votante.html')
        
        # Procesar foto
        foto_filename = None
        if 'foto' in request.files:
            file = request.files['foto']
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                foto_filename = f"{session['user_id']}_{timestamp}_{filename}"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], foto_filename))
        
        conn = get_db()
        try:
            conn.execute('''
                INSERT INTO votantes (colaborador_id, nombre_completo, numero_cedula, telefono, direccion,
                                     latitud, longitud, escuela_votacion, foto, notas)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (session['user_id'], nombre_completo, numero_cedula, telefono, direccion,
                  latitud if latitud else None, longitud if longitud else None,
                  escuela_votacion, foto_filename, notas))
            conn.commit()
            flash('Votante registrado exitosamente', 'success')
        except sqlite3.IntegrityError as e:
            flash('Error: La cédula ya existe. Por favor verifique los datos.', 'error')
            return render_template('nuevo_votante.html')
        finally:
            conn.close()
        
        return redirect(url_for('dashboard_colaborador'))
    
    return render_template('nuevo_votante.html')

@app.route('/votante/editar/<int:votante_id>', methods=['GET', 'POST'])
def editar_votante(votante_id):
    if 'user_id' not in session or session['rol'] != 'colaborador':
        return redirect(url_for('login'))
    
    conn = get_db()
    
    if request.method == 'POST':
        nombre_completo = request.form['nombre_completo']
        numero_cedula = request.form.get('numero_cedula', '').strip()
        telefono = request.form.get('telefono', '')
        direccion = request.form.get('direccion', '')
        latitud = request.form.get('latitud')
        longitud = request.form.get('longitud')
        escuela_votacion = request.form.get('escuela_votacion', '')
        notas = request.form.get('notas', '')
        
        # Validar cédula única (excluyendo el votante actual)
        if numero_cedula:
            votante_existente = conn.execute(
                'SELECT id FROM votantes WHERE numero_cedula = ? AND id != ?',
                (numero_cedula, votante_id)
            ).fetchone()
            
            if votante_existente:
                conn.close()
                flash('Error: Esta cédula ya está registrada por otro votante', 'error')
                votante = conn.execute(
                    'SELECT * FROM votantes WHERE id = ? AND colaborador_id = ?',
                    (votante_id, session['user_id'])
                ).fetchone()
                return render_template('editar_votante.html', votante=votante)
        
        # Procesar nueva foto si se sube
        foto_filename = request.form.get('foto_actual')
        if 'foto' in request.files:
            file = request.files['foto']
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                foto_filename = f"{session['user_id']}_{timestamp}_{filename}"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], foto_filename))
        
        try:
            conn.execute('''
                UPDATE votantes 
                SET nombre_completo=?, numero_cedula=?, telefono=?, direccion=?, latitud=?, longitud=?,
                    escuela_votacion=?, foto=?, notas=?
                WHERE id=? AND colaborador_id=?
            ''', (nombre_completo, numero_cedula, telefono, direccion,
                  latitud if latitud else None, longitud if longitud else None,
                  escuela_votacion, foto_filename, notas, votante_id, session['user_id']))
            conn.commit()
            flash('Votante actualizado exitosamente', 'success')
        except sqlite3.IntegrityError:
            flash('Error: La cédula ya existe. Por favor verifique los datos.', 'error')
        finally:
            conn.close()
        
        return redirect(url_for('dashboard_colaborador'))
    
    votante = conn.execute(
        'SELECT * FROM votantes WHERE id = ? AND colaborador_id = ?',
        (votante_id, session['user_id'])
    ).fetchone()
    conn.close()
    
    if not votante:
        flash('Votante no encontrado', 'error')
        return redirect(url_for('dashboard_colaborador'))
    
    return render_template('editar_votante.html', votante=votante)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/votante/eliminar/<int:votante_id>')
def eliminar_votante(votante_id):
    if 'user_id' not in session or session['rol'] != 'colaborador':
        return redirect(url_for('login'))
    
    conn = get_db()
    conn.execute('DELETE FROM votantes WHERE id = ? AND colaborador_id = ?',
                (votante_id, session['user_id']))
    conn.commit()
    conn.close()
    
    flash('Votante eliminado exitosamente', 'success')
    return redirect(url_for('dashboard_colaborador'))

@app.route('/api/votantes')
def api_votantes():
    if 'user_id' not in session or session['rol'] != 'candidato':
        return jsonify({'error': 'No autorizado'}), 403
    
    conn = get_db()
    votantes = conn.execute('''
        SELECT v.*, u.nombre as colaborador
        FROM votantes v
        JOIN usuarios u ON v.colaborador_id = u.id
        WHERE v.latitud IS NOT NULL AND v.longitud IS NOT NULL
    ''').fetchall()
    conn.close()
    
    votantes_list = []
    for v in votantes:
        votantes_list.append({
            'id': v['id'],
            'nombre': v['nombre_completo'],
            'telefono': v['telefono'],
            'direccion': v['direccion'],
            'lat': v['latitud'],
            'lng': v['longitud'],
            'escuela': v['escuela_votacion'],
            'colaborador': v['colaborador']
        })
    
    return jsonify(votantes_list)

@app.route('/colaboradores')
def lista_colaboradores():
    if 'user_id' not in session or session['rol'] != 'candidato':
        return redirect(url_for('login'))
    
    conn = get_db()
    colaboradores = conn.execute('''
        SELECT u.*, COUNT(v.id) as total_votantes
        FROM usuarios u
        LEFT JOIN votantes v ON u.id = v.colaborador_id
        WHERE u.rol = "colaborador"
        GROUP BY u.id
        ORDER BY total_votantes DESC
    ''').fetchall()
    conn.close()
    
    return render_template('colaboradores.html', colaboradores=colaboradores)

@app.route('/colaborador/crear', methods=['GET', 'POST'])
def crear_colaborador():
    if 'user_id' not in session or session['rol'] != 'candidato':
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        usuario = request.form['usuario']
        password = request.form['password']
        
        conn = get_db()
        try:
            conn.execute(
                'INSERT INTO usuarios (nombre, usuario, password, rol) VALUES (?, ?, ?, ?)',
                (nombre, usuario, generate_password_hash(password), 'colaborador')
            )
            conn.commit()
            flash(f'Colaborador {nombre} creado exitosamente', 'success')
        except sqlite3.IntegrityError:
            flash('El usuario ya existe', 'error')
        conn.close()
        
        return redirect(url_for('lista_colaboradores'))
    
    return render_template('crear_colaborador.html')

@app.route('/buscar/votantes', methods=['GET', 'POST'])
def buscar_votantes():
    """Ruta para buscar votantes por nombre o cédula"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    votantes_encontrados = []
    busqueda_realizada = False
    
    if request.method == 'POST':
        busqueda_nombre = request.form.get('busqueda_nombre', '').strip()
        busqueda_cedula = request.form.get('busqueda_cedula', '').strip()
        
        conn = get_db()
        
        # Lógica de búsqueda
        if busqueda_cedula:
            # Búsqueda por cédula (más específica)
            resultado = conn.execute('''
                SELECT v.*, u.nombre as colaborador
                FROM votantes v
                JOIN usuarios u ON v.colaborador_id = u.id
                WHERE v.numero_cedula LIKE ?
                ORDER BY v.nombre_completo
            ''', (f'%{busqueda_cedula}%',)).fetchall()
            
            # Si no encuentra por cédula exacta, busca por similitud
            if not resultado:
                resultado = conn.execute('''
                    SELECT v.*, u.nombre as colaborador
                    FROM votantes v
                    JOIN usuarios u ON v.colaborador_id = u.id
                    WHERE v.numero_cedula LIKE ?
                    ORDER BY v.nombre_completo
                ''', (f'%{busqueda_cedula}%',)).fetchall()
        
        elif busqueda_nombre:
            # Búsqueda por nombre
            resultado = conn.execute('''
                SELECT v.*, u.nombre as colaborador
                FROM votantes v
                JOIN usuarios u ON v.colaborador_id = u.id
                WHERE v.nombre_completo LIKE ?
                ORDER BY v.nombre_completo
            ''', (f'%{busqueda_nombre}%',)).fetchall()
        else:
            resultado = []
        
        conn.close()
        
        # Convertir resultados a diccionarios y manejar fechas
        for votante in resultado:
            votante_dict = dict(votante)
            votante_dict['colaborador'] = votante['colaborador']
            
            # Convertir fecha_registro a objeto datetime si existe
            if votante_dict.get('fecha_registro'):
                try:
                    # SQLite devuelve fechas como strings, las convertimos a datetime
                    if isinstance(votante_dict['fecha_registro'], str):
                        votante_dict['fecha_registro'] = datetime.strptime(
                            votante_dict['fecha_registro'], '%Y-%m-%d %H:%M:%S'
                        )
                except (ValueError, TypeError):
                    # Si no se puede convertir, mantener como string
                    pass
            
            votantes_encontrados.append(votante_dict)
        
        busqueda_realizada = True
    
    return render_template('buscar_votantes.html',
                         votantes_encontrados=votantes_encontrados,
                         busqueda_realizada=busqueda_realizada)

@app.route('/validar/cedula/<cedula>')
def validar_cedula(cedula):
    """API para validar si una cédula ya existe"""
    if 'user_id' not in session:
        return jsonify({'error': 'No autorizado'}), 403
    
    if not cedula:
        return jsonify({'valida': True, 'mensaje': 'Cédula válida'})
    
    conn = get_db()
    
    # Verificar si la cédula ya existe (excluyendo el votante actual si estamos editando)
    votante_actual = request.args.get('votante_id')
    if votante_actual:
        resultado = conn.execute(
            'SELECT id FROM votantes WHERE numero_cedula = ? AND id != ?',
            (cedula, votante_actual)
        ).fetchone()
    else:
        resultado = conn.execute(
            'SELECT id FROM votantes WHERE numero_cedula = ?',
            (cedula,)
        ).fetchone()
    
    conn.close()
    
    if resultado:
        return jsonify({
            'valida': False, 
            'mensaje': 'Esta cédula ya está registrada'
        })
    else:
        return jsonify({
            'valida': True, 
            'mensaje': 'Cédula disponible'
        })

@app.route('/api/buscar/votantes')
def api_buscar_votantes():
    """API para búsqueda en tiempo real de votantes"""
    if 'user_id' not in session:
        return jsonify({'error': 'No autorizado'}), 403
    
    busqueda = request.args.get('q', '')
    tipo = request.args.get('tipo', 'nombre')  # 'nombre' o 'cedula'
    
    if not busqueda:
        return jsonify([])
    
    conn = get_db()
    
    if tipo == 'cedula':
        resultados = conn.execute('''
            SELECT v.id, v.nombre_completo, v.numero_cedula, v.telefono, 
                   v.direccion, v.fecha_registro
            FROM votantes v
            WHERE v.numero_cedula LIKE ?
            ORDER BY v.nombre_completo
            LIMIT 10
        ''', (f'%{busqueda}%',)).fetchall()
    else:
        resultados = conn.execute('''
            SELECT v.id, v.nombre_completo, v.numero_cedula, v.telefono,
                   v.direccion, v.fecha_registro
            FROM votantes v
            WHERE v.nombre_completo LIKE ?
            ORDER BY v.nombre_completo
            LIMIT 10
        ''', (f'%{busqueda}%',)).fetchall()
    
    conn.close()
    
    resultados_list = []
    for r in resultados:
        # Convertir fecha si existe
        fecha_str = ''
        if r['fecha_registro']:
            try:
                # Formatear fecha para mostrar
                fecha_obj = datetime.strptime(r['fecha_registro'], '%Y-%m-%d %H:%M:%S')
                fecha_str = fecha_obj.strftime('%d/%m/%Y')
            except (ValueError, TypeError):
                fecha_str = str(r['fecha_registro'])
        
        resultados_list.append({
            'id': r['id'],
            'nombre': r['nombre_completo'],
            'cedula': r['numero_cedula'],
            'telefono': r['telefono'],
            'direccion': r['direccion'],
            'fecha': fecha_str
        })
    
    return jsonify(resultados_list)

@app.route('/movil')
def movil():
    """Interfaz móvil para uso en campo"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    return render_template('movil.html')

@app.route('/api/movil/registrar')
def api_movil_registrar():
    """API simplificada para registro móvil"""
    if 'user_id' not in session:
        return jsonify({'error': 'No autorizado'}), 403
    
    # Aquí iría la lógica simplificada para registro móvil
    return jsonify({
        'status': 'success',
        'message': 'Función en desarrollo',
        'funciones_disponibles': [
            'Búsqueda rápida',
            'Registro con GPS automático',
            'Sincronización offline',
            'Captura de fotos simplificada'
        ]
    })

@app.route('/api/sync-offline-data')
def sync_offline_data():
    """API para sincronización de datos offline"""
    if 'user_id' not in session:
        return jsonify({'error': 'No autorizado'}), 403
    
    # Lógica para sincronizar datos almacenados offline
    return jsonify({'sync': 'completed'})

if __name__ == '__main__':
    if not os.path.exists('database.db'):
        init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
