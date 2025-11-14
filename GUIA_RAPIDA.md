# 🎯 Guía Rápida de Inicio

## ⚡ Inicio Rápido (3 pasos)

### Windows:
1. Haz doble clic en `INICIAR_WINDOWS.bat`
2. Espera que se abra la aplicación
3. Ve a http://localhost:5000 en tu navegador

### Linux/Mac:
1. Abre terminal en esta carpeta
2. Ejecuta: `bash INICIAR_LINUX_MAC.sh`
3. Ve a http://localhost:5000 en tu navegador

---

## 👥 Usuarios de Prueba

### 🎩 Candidato (Administrador)
```
Usuario: candidato
Contraseña: admin123
```
**Puede hacer:** Ver todo, crear colaboradores, ver estadísticas y mapas

### 👤 Colaboradores
```
Usuario: juan / maria / carlos
Contraseña: colaborador123
```
**Pueden hacer:** Registrar votantes, subir fotos, marcar ubicaciones

---

## 📱 Funcionalidades Principales

### Como Colaborador puedes:
- ➕ Registrar nuevos votantes
- 📸 Subir fotos de identificación
- 📍 Marcar ubicación de casa en el mapa
- 🏫 Registrar escuela de votación
- ✏️ Editar tus registros
- 📋 Ver lista de tus votantes

### Como Candidato puedes:
- 📊 Ver estadísticas totales
- 🏆 Ver ranking de colaboradores
- 🗺️ Ver mapa con todos los votantes
- 📈 Ver gráficos de desempeño
- ➕ Crear nuevos colaboradores
- 👥 Gestionar equipo de trabajo

---

## 🗺️ Uso del Mapa

1. **Registrar ubicación:**
   - Abre "Nuevo Votante"
   - Haz clic en el mapa donde vive el votante
   - Se colocará un marcador automáticamente

2. **Ver ubicaciones:**
   - El candidato ve todos los votantes en el mapa
   - Haz clic en un marcador para ver información
   - Útil para planificar rutas de transporte

---

## 🚗 Planificación de Logística

La información recopilada sirve para:
- 📍 Ubicar casas de votantes en el mapa
- 🚌 Planificar rutas de transporte el día de votación
- 🏫 Saber a qué escuela debe ir cada votante
- 📱 Contactar votantes por teléfono
- 📊 Distribuir trabajo entre colaboradores

---

## ❓ Problemas Comunes

**"No puedo acceder a http://localhost:5000"**
- Verifica que el servidor esté corriendo (debe decir "Running on...")
- Prueba con http://127.0.0.1:5000

**"Error al instalar dependencias"**
- Asegúrate de tener Python instalado
- Verifica con: `python --version` (Windows) o `python3 --version` (Linux/Mac)

**"El mapa no carga"**
- Verifica tu conexión a internet
- Los mapas se cargan desde OpenStreetMap (gratis)

**"No puedo subir fotos"**
- Verifica que la carpeta `uploads/` exista
- Tamaño máximo: 16MB
- Formatos: JPG, PNG, GIF

---

## 🎓 Tutorial Paso a Paso

### Primer uso como Colaborador:

1. **Inicia sesión** con usuario `juan` y contraseña `colaborador123`

2. **Registra tu primer votante:**
   - Clic en "Nuevo Votante"
   - Escribe el nombre: "Juan Pérez"
   - Teléfono: "0981-123456"
   - Dirección: "Calle Principal 123"
   - Haz clic en el mapa donde vive
   - Escuela: "Escuela Nº 1"
   - Sube una foto (opcional)
   - Clic en "Guardar Votante"

3. **Ve tu registro:**
   - Clic en "Mis Votantes"
   - Verás el votante que acabas de registrar

4. **Edita si es necesario:**
   - Clic en el botón azul de editar
   - Modifica lo que necesites
   - Guarda los cambios

### Primer uso como Candidato:

1. **Inicia sesión** con usuario `candidato` y contraseña `admin123`

2. **Revisa el dashboard:**
   - Verás total de votantes y colaboradores
   - Gráfico de desempeño
   - Ranking de mejores colaboradores

3. **Ve el mapa general:**
   - Todos los votantes aparecen en el mapa
   - Haz clic en los marcadores para ver información

4. **Crea un nuevo colaborador:**
   - Clic en "Colaboradores"
   - Clic en "Nuevo Colaborador"
   - Completa los datos
   - Comparte las credenciales con tu nuevo colaborador

---

## 💡 Consejos

- 📸 **Fotos:** Ayudan a identificar votantes el día de la elección
- 📍 **Ubicación:** Esencial para planificar rutas de transporte
- 📱 **Teléfono:** Para recordarles que vayan a votar
- 🏫 **Escuela:** Evita que vayan al lugar equivocado
- 🏆 **Competencia sana:** El ranking motiva a los colaboradores

---

## 🔐 Seguridad

- ✅ Contraseñas encriptadas
- ✅ Cada colaborador solo ve sus registros
- ✅ Solo el candidato ve todo
- ✅ Sesiones seguras
- ✅ Base de datos local (no en internet)

---

## 📞 ¿Necesitas Ayuda?

Lee el archivo `README.md` para más detalles técnicos y solución de problemas.

---

**¡Todo listo! Comienza a registrar votantes y organiza tu campaña 🚀**
