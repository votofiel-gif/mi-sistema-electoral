"""
Script para agregar datos de ejemplo a la base de datos
Ejecuta este archivo para ver la aplicación con información de prueba
"""

import sqlite3
from datetime import datetime

def agregar_datos_ejemplo():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Datos de ejemplo de votantes para diferentes colaboradores
    votantes_ejemplo = [
        # Votantes de Juan (id: 2)
        (2, 'María Fernández', '0981-111111', 'Av. Eusebio Ayala 1234', -25.2823, -57.6343, 'Escuela República Argentina', 'Muy entusiasta, siempre puntual'),
        (2, 'Roberto Silva', '0982-222222', 'Calle Palma 567', -25.2889, -57.6289, 'Colegio Nacional', 'Necesita transporte'),
        (2, 'Ana Benítez', '0983-333333', 'Av. España 890', -25.2756, -57.6401, 'Escuela San José', 'Puede llevar 3 personas en su auto'),
        (2, 'Carlos Medina', '0984-444444', 'Calle Colón 234', -25.2901, -57.6234, 'Escuela República Argentina', 'Adulto mayor, requiere asistencia'),
        (2, 'Laura Martínez', '0985-555555', 'Av. Mcal. López 456', -25.2834, -57.6312, 'Colegio Nacional', 'Líder comunitario, puede movilizar gente'),
        
        # Votantes de María (id: 3)
        (3, 'Pedro Ramírez', '0986-666666', 'Calle Cerro Corá 789', -25.2945, -57.6178, 'Escuela Nº 1 Mariscal López', 'Muy activo en redes sociales'),
        (3, 'Sofía Acosta', '0987-777777', 'Av. Artigas 1011', -25.2712, -57.6445, 'Colegio Técnico Nacional', 'Estudiante universitaria'),
        (3, 'Javier Coronel', '0988-888888', 'Calle Paraguarí 1213', -25.2867, -57.6267, 'Escuela República del Perú', 'Comerciante del mercado'),
        (3, 'Claudia Vera', '0989-999999', 'Av. Brasil 1415', -25.2790, -57.6378, 'Escuela San José', 'Enfermera, termina turno a las 14hs'),
        
        # Votantes de Carlos (id: 4)
        (4, 'Diego Flores', '0991-111222', 'Calle Yegros 1617', -25.2923, -57.6201, 'Colegio Nacional', 'Profesor, puede ayudar con fiscalización'),
        (4, 'Patricia Sánchez', '0992-333444', 'Av. San Martín 1819', -25.2778, -57.6423, 'Escuela República Argentina', 'Tiene familiares en el barrio'),
        (4, 'Fernando Cabrera', '0993-555666', 'Calle Montevideo 2021', -25.2845, -57.6334, 'Escuela Nº 1 Mariscal López', 'Taxista, puede ayudar con transporte'),
    ]
    
    print("Agregando votantes de ejemplo...")
    
    for votante in votantes_ejemplo:
        try:
            cursor.execute('''
                INSERT INTO votantes (colaborador_id, nombre_completo, telefono, direccion,
                                     latitud, longitud, escuela_votacion, notas, fecha_registro)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (*votante, datetime.now()))
            print(f"✓ Agregado: {votante[1]}")
        except sqlite3.IntegrityError:
            print(f"⚠ Ya existe: {votante[1]}")
    
    conn.commit()
    
    # Mostrar estadísticas
    cursor.execute('SELECT COUNT(*) FROM votantes')
    total = cursor.fetchone()[0]
    
    cursor.execute('''
        SELECT u.nombre, COUNT(v.id) 
        FROM usuarios u 
        LEFT JOIN votantes v ON u.id = v.colaborador_id 
        WHERE u.rol = "colaborador" 
        GROUP BY u.id, u.nombre
    ''')
    stats = cursor.fetchall()
    
    conn.close()
    
    print("\n" + "="*50)
    print("📊 ESTADÍSTICAS:")
    print("="*50)
    print(f"Total de votantes: {total}")
    print("\nVotantes por colaborador:")
    for nombre, count in stats:
        print(f"  - {nombre}: {count} votantes")
    print("="*50)
    print("\n✅ Datos de ejemplo agregados exitosamente!")
    print("\nAhora puedes:")
    print("1. Iniciar la aplicación")
    print("2. Iniciar sesión como 'candidato' / 'admin123'")
    print("3. Ver el mapa con todos los votantes")
    print("4. Ver estadísticas y gráficos con datos reales")

if __name__ == '__main__':
    agregar_datos_ejemplo()
