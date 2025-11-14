#!/bin/bash

# Script de inicio rápido para probar la búsqueda en tiempo real
echo "🚀 INICIANDO SISTEMA CON BÚSQUEDA EN TIEMPO REAL"
echo "=================================================="
echo ""
echo "🔧 Verificando dependencias..."
python3 -c "
try:
    import flask, sqlite3
    print('✅ Dependencias OK')
except ImportError:
    print('❌ Instalando dependencias...')
    import subprocess
    subprocess.run(['python3', '-m', 'pip', 'install', 'flask'], check=True)
"

echo ""
echo "🔍 Verificando base de datos..."
python3 demo_buscador.py | head -20

echo ""
echo "🌟 CARACTERÍSTICAS IMPLEMENTADAS:"
echo "✅ Búsqueda en tiempo real (mientras escribes)"
echo "✅ Corrección del error de fechas"
echo "✅ Debounce optimizado"
echo "✅ Indicadores de carga"
echo "✅ Información detallada en resultados"
echo "✅ Navegación fluida"
echo ""
echo "🎯 Para acceder al buscador:"
echo "   1. Ejecuta: python3 app.py"
echo "   2. Ve a: http://localhost:5000/buscar/votantes"
echo "   3. ¡Empieza a escribir y ve los resultados en tiempo real!"
echo ""
echo "📚 Documentación: GUIA_BUSQUEDA_TIEMPO_REAL.md"
echo "🔧 Pruebas: python3 probar_busqueda_tiempo_real.py"