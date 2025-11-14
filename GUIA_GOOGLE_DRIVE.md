# 🔄 Guía para Sincronizar Base de Datos con Google Drive

## 📍 Ubicación Actual
La base de datos está en: `app-votantes/database.db`

## 🚀 Solución Recomendada: Sincronización Automática

### Paso 1: Crear Carpeta en Google Drive
1. Ve a Google Drive (drive.google.com)
2. Crea una carpeta llamada: `Campaña-Votantes`
3. Anota la ubicación exacta: `Google Drive/Campaña-Votantes`

### Paso 2: Configurar Sincronización en tu Computador
1. **Instala Google Drive Desktop** (si no lo tienes)
2. **Vincula la carpeta** `app-votantes` con Google Drive
3. La sincronización será automática

### Paso 3: Ejecutar Script de Sincronización
Ejecuta este script después de cada sesión de trabajo:
```bash
# En la carpeta app-votantes/
python3 sincronizar_google_drive.py
```

## 📁 Estructura de Archivos Sincronizados
```
Google Drive/Campaña-Votantes/
├── database.db          # Base de datos principal
├── backups/             # Respaldos automáticos
│   ├── database_2025-11-14.db
│   ├── database_2025-11-13.db
│   └── ...
└── exports/             # Exportaciones para análisis
    ├── votantes_excel.csv
    ├── resumen_mensual.xlsx
    └── ...
```

## 🔧 Scripts Incluidos
- `sincronizar_google_drive.py` - Sincronización manual
- `backup_automatico.py` - Respaldos programados  
- `exportar_datos.py` - Exportar para análisis externo