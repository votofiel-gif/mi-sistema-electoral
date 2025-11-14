#!/bin/bash
# Script de inicio para el Sistema de Gestión de Votantes con Buscador y Cédula Única

echo "🚀 SISTEMA DE GESTIÓN DE VOTANTES"
echo "🔍 Con Buscador de Votantes y Validación de Cédula Única"
echo "========================================"

# Verificar si existe la base de datos
if [ ! -f "database.db" ]; then
    echo "📋 Inicializando base de datos..."
    python app.py &
    sleep 3
    pkill -f "python app.py"
    echo "✅ Base de datos creada"
fi

echo ""
echo "🔍 FUNCIONALIDADES IMPLEMENTADAS:"
echo "   ✓ Buscador de votantes por nombre y cédula"
echo "   ✓ Validación de cédula única"
echo "   ✓ Validación en tiempo real"
echo "   ✓ APIs de búsqueda"
echo "   ✓ Interfaz moderna y responsive"
echo ""
echo "🌐 Para acceder al sistema:"
echo "   1. Abre tu navegador"
echo "   2. Ve a: http://localhost:5000"
echo "   3. Usuario: candidato / Contraseña: admin123"
echo "   4. O usuario: juan / Contraseña: colaborador123"
echo ""
echo "🔍 Para usar el buscador:"
echo "   - Busca en la barra de navegación 'Buscar'"
echo "   - O usa los botones en los dashboards"
echo ""
echo "🔒 Validación de cédula:"
echo "   - Se valida automáticamente al crear/editar"
echo "   - No se permiten cédulas duplicadas"
echo ""
echo "========================================"
echo "🟢 Iniciando servidor..."
echo "========================================"

# Ejecutar la aplicación
python app.py