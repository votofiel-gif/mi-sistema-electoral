# 📦 APLICACIÓN COMPLETADA - Sistema de Gestión de Votantes

## ✅ ESTADO: LISTA PARA USAR

---

## 🎯 ¿Qué tienes?

Una aplicación web completa para gestionar votantes en campañas electorales con:

✅ Sistema de login con usuarios y contraseñas
✅ Panel para colaboradores (registrar votantes)
✅ Panel para candidato (ver estadísticas e informes)
✅ Mapas interactivos con ubicaciones
✅ Subida de fotos de votantes
✅ Gráficos de desempeño
✅ Ranking de colaboradores
✅ Base de datos incluida
✅ 4 usuarios de prueba precargados

---

## 🚀 CÓMO INICIAR LA APLICACIÓN

### OPCIÓN 1: Usar los scripts de inicio (MÁS FÁCIL)

**En Windows:**
1. Haz doble clic en `INICIAR_WINDOWS.bat`
2. Espera que diga "Running on..."
3. Abre tu navegador en: http://localhost:5000

**En Linux/Mac:**
1. Abre terminal en la carpeta del proyecto
2. Ejecuta: `bash INICIAR_LINUX_MAC.sh`
3. Abre tu navegador en: http://localhost:5000

### OPCIÓN 2: Manualmente

**Paso 1 - Instalar dependencias (solo la primera vez):**
```bash
# Windows
pip install -r requirements.txt

# Linux/Mac
pip3 install -r requirements.txt
```

**Paso 2 - Iniciar servidor:**
```bash
# Windows
python app.py

# Linux/Mac
python3 app.py
```

**Paso 3 - Abrir navegador:**
Ve a http://localhost:5000

---

## 👥 USUARIOS PARA PROBAR

### 🎩 Candidato (Administrador)
```
Usuario: candidato
Contraseña: admin123
```
**Puede:**
- Ver dashboard con estadísticas
- Ver mapa con todos los votantes
- Ver ranking de colaboradores
- Crear nuevos colaboradores
- Ver gráficos de desempeño

### 👤 Colaboradores
```
Usuario: juan
Contraseña: colaborador123

Usuario: maria
Contraseña: colaborador123

Usuario: carlos
Contraseña: colaborador123
```
**Pueden:**
- Registrar nuevos votantes
- Subir fotos
- Marcar ubicaciones en el mapa
- Ver sus propios registros
- Editar/eliminar sus votantes

---

## 📱 FUNCIONALIDADES PRINCIPALES

### Para Colaboradores:
1. **Registrar Votantes**
   - Nombre, teléfono, dirección
   - Ubicación en mapa (clic para marcar)
   - Foto del votante
   - Escuela donde votará
   - Notas adicionales

2. **Gestionar Registros**
   - Ver lista de votantes registrados
   - Editar información
   - Eliminar registros

### Para Candidato:
1. **Dashboard con Estadísticas**
   - Total de votantes registrados
   - Total de colaboradores activos
   - Gráfico de desempeño por colaborador
   - Ranking de mejores colaboradores

2. **Mapa General**
   - Ver todos los votantes en un mapa
   - Hacer clic en marcadores para ver info
   - Útil para planificar rutas de transporte

3. **Gestión de Colaboradores**
   - Crear nuevos colaboradores
   - Ver cuántos votantes registró cada uno
   - Asignar credenciales de acceso

---

## 🗺️ USO DEL MAPA

**Para marcar una ubicación:**
1. Al registrar un votante, verás un mapa
2. Haz clic donde vive el votante
3. Se colocará un marcador automáticamente
4. La ubicación se guarda con el registro

**El mapa sirve para:**
- Ubicar casas de votantes
- Planificar rutas de transporte el día de votación
- Ver distribución geográfica de votantes
- Organizar logística de movilización

---

## 📂 ARCHIVOS DEL PROYECTO

```
app-votantes/
├── app.py                          # ⚙️ Servidor principal (NO MODIFICAR)
├── database.db                     # 💾 Base de datos (se crea solo)
├── requirements.txt                # 📦 Dependencias de Python
├── README.md                       # 📖 Documentación completa
├── GUIA_RAPIDA.md                 # 🎯 Guía rápida de uso
├── INSTRUCCIONES_COMPLETAS.md     # 📋 Este archivo
├── INICIAR_WINDOWS.bat            # 🪟 Script para Windows
├── INICIAR_LINUX_MAC.sh           # 🐧 Script para Linux/Mac
├── templates/                      # 🎨 Páginas HTML
│   ├── base.html
│   ├── login.html
│   ├── dashboard_candidato.html
│   ├── dashboard_colaborador.html
│   ├── nuevo_votante.html
│   ├── editar_votante.html
│   ├── colaboradores.html
│   └── crear_colaborador.html
├── static/                         # 📁 Archivos estáticos
│   ├── css/
│   ├── js/
│   └── images/
└── uploads/                        # 📸 Fotos de votantes
```

---

## 🎓 TUTORIAL PASO A PASO

### PRIMER USO - Como Colaborador:

**1. Inicia sesión**
- Usuario: `juan`
- Contraseña: `colaborador123`

**2. Registra tu primer votante**
- Clic en "Nuevo Votante"
- Completa los datos:
  - Nombre: "Pedro Gómez"
  - Teléfono: "0981-123456"
  - Dirección: "Av. Principal 456"
  - Haz clic en el mapa donde vive
  - Escuela: "Escuela República de Chile"
  - Sube una foto (opcional)
- Clic en "Guardar Votante"

**3. Verifica tu registro**
- Clic en "Mis Votantes"
- Verás el votante que acabas de crear

### PRIMER USO - Como Candidato:

**1. Inicia sesión**
- Usuario: `candidato`
- Contraseña: `admin123`

**2. Explora el dashboard**
- Verás estadísticas totales
- Gráfico de desempeño
- Ranking de colaboradores

**3. Ve el mapa general**
- Todos los votantes aparecen con marcadores
- Haz clic en marcadores para ver información

**4. Crea un colaborador nuevo**
- Clic en "Colaboradores" → "Nuevo Colaborador"
- Nombre: "Ana López"
- Usuario: "ana"
- Contraseña: "mipassword123"
- Clic en "Crear Colaborador"
- Comparte las credenciales con Ana

---

## ❓ PREGUNTAS FRECUENTES

**P: ¿Necesito internet?**
R: Sí, solo para cargar los mapas. La aplicación funciona localmente.

**P: ¿Los datos están seguros?**
R: Sí, todo se guarda en tu computadora (database.db). No se envía nada a internet.

**P: ¿Puedo cambiar las contraseñas?**
R: Sí, al crear nuevos colaboradores puedes poner las contraseñas que quieras.

**P: ¿Cuántos colaboradores puedo crear?**
R: Ilimitados.

**P: ¿Cuántos votantes puedo registrar?**
R: Ilimitados.

**P: ¿Funciona en celular?**
R: Sí, el diseño es responsive y funciona en cualquier dispositivo.

**P: ¿Puedo usar esto en mi campaña real?**
R: ¡Sí! Está diseñado específicamente para eso.

---

## 🔧 SOLUCIÓN DE PROBLEMAS

**Problema: "No puedo acceder a localhost:5000"**
Solución:
- Verifica que el servidor esté corriendo (debe decir "Running on...")
- Prueba con http://127.0.0.1:5000
- Asegúrate de que no haya otra aplicación usando el puerto 5000

**Problema: "No module named Flask"**
Solución:
- Ejecuta: `pip install -r requirements.txt` (Windows)
- O: `pip3 install -r requirements.txt` (Linux/Mac)

**Problema: "El mapa no carga"**
Solución:
- Verifica tu conexión a internet
- Los mapas vienen de OpenStreetMap (gratis)
- Recarga la página

**Problema: "No puedo subir fotos"**
Solución:
- Verifica que la carpeta `uploads/` exista
- Tamaño máximo: 16MB
- Formatos válidos: JPG, PNG, GIF

**Problema: "Olvidé la contraseña"**
Solución:
- Elimina el archivo `database.db`
- Reinicia la aplicación
- Se crearán los usuarios de prueba nuevamente

---

## 🎯 CASOS DE USO

### Día a día durante la campaña:
1. Colaboradores salen a la calle
2. Conocen votantes interesados
3. Registran sus datos en la app
4. Toman foto para identificarlos
5. Marcan la casa en el mapa
6. El candidato ve el progreso en tiempo real

### Día de la elección:
1. El candidato revisa el mapa
2. Ve todas las ubicaciones de votantes
3. Planifica rutas de transporte
4. Asigna colaboradores a zonas
5. Llama a votantes para recordarles
6. Coordina movilización a escuelas

---

## 💡 CONSEJOS DE USO

✅ **Fotos:** Ayudan a identificar votantes el día de la elección
✅ **Ubicación:** Esencial para organizar transporte
✅ **Teléfono:** Para recordarles que vayan a votar
✅ **Escuela:** Evita confusiones sobre dónde votar
✅ **Notas:** Agrega cualquier información útil
✅ **Competencia:** El ranking motiva a los colaboradores

---

## 🔐 SEGURIDAD

✅ Contraseñas encriptadas en la base de datos
✅ Cada colaborador solo ve sus propios registros
✅ Solo el candidato tiene acceso completo
✅ Sesiones seguras con cookies
✅ Los datos no salen de tu computadora

---

## 📊 TECNOLOGÍAS USADAS

- **Backend:** Python + Flask (simple y poderoso)
- **Base de datos:** SQLite (no requiere instalación)
- **Mapas:** Leaflet + OpenStreetMap (gratis)
- **Diseño:** Bootstrap 5 (responsive)
- **Gráficos:** Chart.js (interactivos)
- **Iconos:** Font Awesome (profesionales)

---

## 🎨 PERSONALIZACIÓN

### Cambiar el puerto (si 5000 está ocupado):
Edita `app.py` última línea:
```python
app.run(debug=True, host='0.0.0.0', port=8080)
```

### Cambiar ubicación del mapa por defecto:
En `nuevo_votante.html` línea 113:
```javascript
map.setView([-25.2637, -57.5759], 13);
// Cambia por las coordenadas de tu ciudad
```

### Cambiar colores del diseño:
En `templates/base.html` línea 9-14:
```css
:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    /* Cambia estos valores */
}
```

---

## 📞 ¿NECESITAS MÁS AYUDA?

Revisa estos archivos en orden:
1. `GUIA_RAPIDA.md` - Para empezar rápido
2. `README.md` - Documentación completa
3. Este archivo - Instrucciones detalladas

Si hay errores:
- Lee el mensaje de error completo
- Busca en este archivo la solución
- Verifica que Python esté instalado correctamente

---

## ✨ CARACTERÍSTICAS DESTACADAS

🎯 **Fácil de usar** - Sin conocimientos técnicos necesarios
🚀 **Rápida** - Carga y funciona en segundos
💾 **Local** - Tus datos no van a internet
🗺️ **Mapas interactivos** - Visualización geográfica
📊 **Estadísticas** - Gráficos y ranking en tiempo real
📱 **Responsive** - Funciona en PC, tablet y móvil
🔒 **Segura** - Contraseñas encriptadas
👥 **Multiusuario** - Colaboradores ilimitados
📸 **Con fotos** - Identifica fácilmente a votantes
🆓 **Gratis** - 100% gratuita, sin costos ocultos

---

## 🎉 ¡LISTO PARA USAR!

Tu aplicación está **100% funcional** y lista para tu campaña.

**Siguiente paso:**
1. Ejecuta `INICIAR_WINDOWS.bat` o `bash INICIAR_LINUX_MAC.sh`
2. Abre http://localhost:5000
3. Inicia sesión y comienza a registrar votantes

**¡Éxito en tu campaña electoral! 🗳️🎊**

---

**Fecha de creación:** 2025
**Versión:** 1.0
**Desarrollado con:** Python + Flask
**Licencia:** Uso libre para campañas electorales
