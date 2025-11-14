@echo off
echo ========================================
echo  Sistema de Gestion de Votantes
echo ========================================
echo.
echo Instalando dependencias...
pip install -r requirements.txt
echo.
echo Iniciando servidor...
echo.
echo La aplicacion estara disponible en:
echo http://localhost:5000
echo.
echo Presiona Ctrl+C para detener el servidor
echo.
python app.py
pause
