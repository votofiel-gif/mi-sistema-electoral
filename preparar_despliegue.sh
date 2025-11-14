#!/bin/bash

echo "🚀 PREPARACIÓN PARA DESPLIEGUE EN LA NUBE"
echo "========================================"

echo ""
echo "📋 ¿Qué necesitamos para que funcione en cualquier dispositivo?"
echo "1. Servidor web público (Render, Railway, etc.)"
echo "2. Aplicación optimizada para móvil (PWA)"
echo "3. Base de datos en la nube"
echo ""

echo "🔧 PREPARANDO ARCHIVOS..."
echo ""

# Crear requirements.txt para el despliegue
echo "📦 Creando requirements.txt..."
cat > requirements.txt << EOF
Flask==2.3.3
Werkzeug==2.3.7
Jinja2==3.1.2
MarkupSafe==2.1.3
click==8.1.7
gunicorn==21.2.0
itsdangerous==2.1.2
Jinja2-cli==0.6.2
MarkupSafe==2.1.3
EOF

# Crear Procfile para Render
echo "📄 Creando Procfile para Render..."
echo "web: gunicorn app:app" > Procfile

# Crear .gitignore
echo "📄 Creando .gitignore..."
cat > .gitignore << EOF
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.env
.venv
pip-log.txt
*.log
database.db
uploads/*
backups/
exports/
*.db
*.xlsx
*.csv
*.json
EOF

# Crear configuración de despliegue
echo "📄 Creando render.yaml..."
cat > render.yaml << EOF
services:
  - type: web
    name: app-votantes-campana
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: FLASK_ENV
        value: production
    autoDeploy: true
EOF

echo "✅ ARCHIVOS CREADOS:"
echo "   • requirements.txt (dependencias)"
echo "   • Procfile (configuración de Render)"
echo "   • .gitignore (archivos a ignorar)"
echo "   • render.yaml (configuración automática)"
echo ""

echo "🎯 OPCIONES DE DESPLIEGUE:"
echo ""
echo "1️⃣ RENDER.COM (Recomendado - GRATIS)"
echo "   • Ve a: https://render.com"
echo "   • Crea cuenta gratuita"
echo "   • Conecta tu repositorio GitHub"
echo "   • ¡Despliegue automático!"
echo "   • URL: https://tu-app.onrender.com"
echo ""

echo "2️⃣ RAILWAY.APP (También GRATIS)"
echo "   • Ve a: https://railway.app"
echo "   • Deploy from GitHub"
echo "   • URL: https://tu-app.railway.app"
echo ""

echo "📱 VERSIÓN MÓVIL INCLUIDA:"
echo "   • URL móvil: https://tu-app.onrender.com/movil"
echo "   • PWA: Instalable como app nativa"
echo "   • Offline: Funciona sin internet"
echo ""

echo "🔗 DESPUÉS DEL DESPLIEGUE:"
echo "   • Todos tus colaboradores pueden acceder"
echo "   • Funciona en cualquier dispositivo"
echo "   • Base de datos se sincroniza automáticamente"
echo "   • Google Drive puede seguir funcionando"
echo ""

echo "⚡ SIGUIENTE PASO:"
echo "   1. Sube el proyecto a GitHub"
echo "   2. Conecta con Render.com"
echo "   3. ¡Listo! URL pública para todos"
echo ""

echo "🆘 ¿Necesitas ayuda?"
echo "   • Documentación: GUIA_DESPLIEGUE_COMPLETA.md"
echo "   • Versión móvil: /movil"
echo "   • Búsqueda en tiempo real: /buscar/votantes"