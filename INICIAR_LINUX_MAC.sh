#!/bin/bash
echo "========================================"
echo " Sistema de Gestión de Votantes"
echo "========================================"
echo ""
echo "Instalando dependencias..."
pip3 install -r requirements.txt
echo ""
echo "Iniciando servidor..."
echo ""
echo "La aplicación estará disponible en:"
echo "http://localhost:5000"
echo ""
echo "Presiona Ctrl+C para detener el servidor"
echo ""
python3 app.py
