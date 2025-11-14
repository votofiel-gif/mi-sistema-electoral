#!/bin/bash

# 🎯 SOLUCIÓN COMPLETA PARA GOOGLE DRIVE
echo "🔗 CONFIGURACIÓN DE SINCRONIZACIÓN CON GOOGLE DRIVE"
echo "=================================================="

echo ""
echo "📍 UBICACIÓN DE TU BASE DE DATOS:"
echo "   $(pwd)/database.db"
echo ""

echo "🚀 OPCIONES DISPONIBLES:"
echo ""
echo "1️⃣ OPCIÓN FÁCIL - Sincronización Manual:"
echo "   • Crea carpeta 'Campaña-Votantes' en tu Google Drive"
echo "   • Copia toda la carpeta 'app-votantes' dentro"
echo "   • ¡Sincronización automática!"
echo ""

echo "2️⃣ OPCIÓN SEMI-AUTOMÁTICA - Script de Backup:"
echo "   python3 sincronizar_google_drive.py"
echo "   • Crea backups automáticos"
echo "   • Exporta datos a Excel/CSV"
echo "   • Genera reportes"
echo ""

echo "3️⃣ OPCIÓN AVANZADA - API de Google Drive:"
echo "   python3 google_drive_config.py"
echo "   • Requiere configuración de Google Cloud Console"
echo "   • Sincronización 100% automática"
echo ""

echo "📋 PASOS RECOMENDADOS:"
echo ""
echo "PASO 1 - Backup inmediato:"
echo "   python3 backup_automatico.py"
echo ""

echo "PASO 2 - Exportar datos para análisis:"
echo "   python3 sincronizar_google_drive.py"
echo ""

echo "PASO 3 - Subir a Google Drive:"
echo "   • Ve a drive.google.com"
echo "   • Crea carpeta 'Campaña-Votantes'"
echo "   • Arrastra las carpetas 'backups' y 'exports'"
echo ""

echo "🎯 ESTRUCTURA FINAL EN GOOGLE DRIVE:"
echo "Google Drive/Campaña-Votantes/"
echo "├── database.db                    # Base de datos principal"
echo "├── backups/                       # Respaldos automáticos"
echo "├── exports/                       # Datos para análisis"
echo "└── [otros archivos de la app]"
echo ""

echo "💡 CONSEJOS DE SEGURIDAD:"
echo "• Haz backup antes de cambios importantes"
echo "• Mantén al menos 3 respaldos en la nube"
echo "• Exporta datos regularmente para análisis"
echo "• Comparte solo con personas autorizadas"
echo ""

echo "🔧 EJECUTAR AHORA:"
echo "   bash configurar_google_drive.sh"
echo ""

# Preguntar si quiere ejecutar configuración
read -p "¿Quieres ejecutar la configuración ahora? (s/n): " respuesta
case $respuesta in
    [Ss]* )
        echo "🚀 Ejecutando backup automático..."
        python3 backup_automatico.py
        echo ""
        echo "🚀 Ejecutando sincronización..."
        python3 sincronizar_google_drive.py
        echo ""
        echo "✅ ¡Listo! Ahora ve a Google Drive para subir los archivos"
        ;;
    [Nn]* )
        echo "👍 Perfecto. Ejecuta cuando quieras:"
        echo "   python3 backup_automatico.py"
        echo "   python3 sincronizar_google_drive.py"
        ;;
    * )
        echo "👍 Ejecuta los scripts cuando quieras"
        ;;
esac