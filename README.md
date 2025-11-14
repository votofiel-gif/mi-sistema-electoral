# 🗳️ Sistema de Gestión de Votantes

Sistema web completo para gestionar votantes en campañas electorales, con mapas interactivos, gestión de colaboradores y panel de estadísticas.

## 📋 Características

### Para Colaboradores:
- ✅ Registro de votantes con datos personales
- 📱 Captura de teléfono y dirección
- 📍 Ubicación en mapa interactivo
- 📸 Subida de fotos
- 🏫 Registro de escuela de votación
- ✏️ Edición y eliminación de registros propios

### Para Candidatos:
- 📊 Dashboard con estadísticas generales
- 🏆 Ranking de desempeño de colaboradores
- 🗺️ Mapa general con todos los votantes
- 📈 Gráficos de rendimiento
- 👥 Gestión de colaboradores
- 📋 Informes detallados

## 🚀 Instalación y Uso

### Requisitos Previos
- Python 3.7 o superior instalado en tu computadora
- Navegador web moderno (Chrome, Firefox, Edge)

### Paso 1: Instalar Python (si no lo tienes)

**Windows:**
1. Ve a https://www.python.org/downloads/
2. Descarga Python 3.11 o superior
3. Durante la instalación, marca "Add Python to PATH"
4. Instala normalmente

**Linux/Mac:**
Python generalmente viene preinstalado. Verifica con:
```bash
python3 --version
```

### Paso 2: Instalar las Dependencias

Abre una terminal o símbolo del sistema en la carpeta del proyecto y ejecuta:

**Windows:**
```bash
pip install -r requirements.txt
```

**Linux/Mac:**
```bash
pip3 install -r requirements.txt
```

### Paso 3: Iniciar la Aplicación

**Windows:**
```bash
python app.py
```

**Linux/Mac:**
```bash
python3 app.py
```

### Paso 4: Acceder a la Aplicación

1. Abre tu navegador web
2. Ve a: http://localhost:5000
3. ¡Listo! Ya puedes usar la aplicación

## 👤 Usuarios de Prueba

La aplicación viene con usuarios precargados para que puedas probar:

### Candidato (Administrador):
- **Usuario:** `candidato`
- **Contraseña:** `admin123`
- **Permisos:** Ver todo, crear colaboradores, ver estadísticas

### Colaboradores:
- **Usuario:** `juan` / **Contraseña:** `colaborador123`
- **Usuario:** `maria` / **Contraseña:** `colaborador123`
- **Usuario:** `carlos` / **Contraseña:** `colaborador123`
- **Permisos:** Registrar y gestionar votantes

## 📂 Estructura del Proyecto

```
app-votantes/
├── app.py                      # Servidor principal
├── database.db                 # Base de datos (se crea automáticamente)
├── requirements.txt            # Dependencias de Python
├── templates/                  # Páginas HTML
│   ├── base.html
│   ├── login.html
│   ├── dashboard_candidato.html
│   ├── dashboard_colaborador.html
│   ├── nuevo_votante.html
│   ├── editar_votante.html
│   ├── colaboradores.html
│   └── crear_colaborador.html
├── static/                     # Archivos estáticos
│   ├── css/
│   ├── js/
│   └── images/
└── uploads/                    # Fotos de votantes
```

## 🎯 Guía de Uso

### Como Candidato:

1. **Inicio de Sesión:** Ingresa con usuario `candidato` y contraseña `admin123`
2. **Dashboard:** Verás estadísticas totales y ranking de colaboradores
3. **Mapa General:** Visualiza todos los votantes registrados en el mapa
4. **Colaboradores:** Crea nuevos colaboradores o gestiona los existentes
5. **Informes:** Revisa el desempeño de cada colaborador

### Como Colaborador:

1. **Inicio de Sesión:** Ingresa con tu usuario y contraseña
2. **Registrar Votante:**
   - Haz clic en "Nuevo Votante"
   - Completa los datos del votante
   - Haz clic en el mapa para marcar su casa
   - Sube una foto (opcional)
   - Guarda el registro
3. **Gestionar Votantes:** Edita o elimina tus registros desde "Mis Votantes"

## 🗺️ Uso del Mapa

- **Marcar Ubicación:** Haz clic en cualquier punto del mapa
- **El mapa usa tu ubicación:** Si permites el acceso, se centrará en tu ubicación
- **Marcadores:** Cada votante aparece como un marcador en el mapa
- **Información:** Haz clic en un marcador para ver los datos del votante

## 🔒 Seguridad

- Las contraseñas se almacenan encriptadas
- Cada colaborador solo puede ver y editar sus propios registros
- El candidato tiene acceso completo a toda la información
- La sesión expira al cerrar el navegador

## 📱 Características Técnicas

- **Framework:** Flask (Python)
- **Base de Datos:** SQLite (no requiere instalación adicional)
- **Mapas:** Leaflet con OpenStreetMap (gratuito)
- **Interfaz:** Bootstrap 5 (responsive)
- **Gráficos:** Chart.js
- **Iconos:** Font Awesome

## 🛠️ Personalización

### Cambiar el Puerto (si 5000 está ocupado):

Edita la última línea de `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=8080)  # Cambia 5000 por el puerto que quieras
```

### Cambiar Ubicación del Mapa por Defecto:

En `nuevo_votante.html` y `dashboard_candidato.html`, busca:
```javascript
map.setView([-25.2637, -57.5759], 13);  // Latitud, Longitud, Zoom
```

Cambia las coordenadas por las de tu ciudad.

## 🐛 Solución de Problemas

### Error: "Puerto ya en uso"
Cambia el puerto en app.py o cierra otras aplicaciones que usen el puerto 5000

### Error: "No module named Flask"
Instala las dependencias: `pip install -r requirements.txt`

### Error: "Permission denied" en uploads/
Verifica que la carpeta uploads/ tenga permisos de escritura

### El mapa no se carga
Verifica tu conexión a internet (los mapas se cargan desde OpenStreetMap)

## 📞 Contacto y Soporte

Si tienes problemas o preguntas, revisa:
1. Esta documentación
2. Los mensajes de error en la terminal
3. La consola del navegador (F12)

## 📄 Licencia

Este proyecto es de código abierto y puede ser usado libremente para campañas electorales.

---

**¡Éxito en tu campaña! 🎉**
