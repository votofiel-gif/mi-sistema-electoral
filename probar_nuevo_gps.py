#!/usr/bin/env python3
"""
Script para demostrar y probar la nueva funcionalidad GPS con confirmación
Ejecuta la aplicación y muestra cómo probar la nueva funcionalidad
"""

import os
import time
import webbrowser
from pathlib import Path

def mostrar_instrucciones():
    """Muestra las instrucciones para probar la nueva funcionalidad GPS"""
    print("=" * 70)
    print("🎯 NUEVA FUNCIONALIDAD GPS CON CONFIRMACIÓN - LISTA PARA PROBAR")
    print("=" * 70)
    
    print("\n📋 ¿QUÉ SE HA CAMBIADO?")
    print("-" * 30)
    print("✅ ANTES: GPS se 'guardaba solo' sin verificación")
    print("✅ AHORA: GPS muestra confirmación antes de aplicar")
    
    print("\n🚀 CÓMO PROBAR LA NUEVA FUNCIONALIDAD:")
    print("-" * 45)
    print("1. 🔑 Inicia sesión como colaborador")
    print("2. ➕ Ve a 'Nuevo Votante' o 'Editar Votante'") 
    print("3. 📍 Haz clic en el botón GPS (📍) en el mapa")
    print("4. ⏳ Espera la confirmación (mostrará las coordenadas)")
    print("5. ✅ Elige una opción:")
    print("   • 'Aplicar GPS' - usa las coordenadas GPS")
    print("   • 'Cancelar' - descarta GPS y sigue manual")
    print("   • 'Intentar de nuevo' - nueva lectura GPS")
    print("6. 💾 Solo se guarda cuando hagas clic en 'Guardar'")
    
    print("\n🎨 INDICADORES VISUALES:")
    print("-" * 25)
    print("• Botón GPS naranja + girando = Obteniendo coordenadas")
    print("• Marcador rojo temporal = GPS obtenido (pendiente)")
    print("• Ventana confirmación = Tú decides qué hacer")
    print("• Marcador azul permanente = GPS aplicado")
    
    print("\n🔧 BENEFICIOS:")
    print("-" * 15)
    print("✓ Control total sobre las coordenadas")
    print("✓ Verificación antes de aplicar")
    print("✓ Flexibilidad manual + GPS")
    print("✓ Auto-cancelación si no hay acción (15 seg)")
    
    print("\n" + "=" * 70)

def verificar_archivos():
    """Verifica que todos los archivos necesarios estén en su lugar"""
    print("\n🔍 VERIFICANDO ARCHIVOS...")
    
    archivos_requeridos = [
        "/workspace/app-votantes/templates/base.html",
        "/workspace/app-votantes/templates/nuevo_votante.html", 
        "/workspace/app-votantes/templates/editar_votante.html",
        "/workspace/app-votantes/GPS_CONFIRMACION.md",
        "/workspace/app-votantes/probar_gps_confirmacion.py"
    ]
    
    todos_presentes = True
    for archivo in archivos_requeridos:
        if os.path.exists(archivo):
            print(f"  ✅ {os.path.basename(archivo)}")
        else:
            print(f"  ❌ {os.path.basename(archivo)} - NO ENCONTRADO")
            todos_presentes = False
    
    return todos_presentes

def ejecutar_aplicacion():
    """Ejecuta la aplicación Flask"""
    print("\n🚀 INICIANDO APLICACIÓN...")
    print("📍 La aplicación estará disponible en: http://127.0.0.1:5000")
    print("🔑 Usa las credenciales: colaborador1 / password")
    
    # Cambiar al directorio de la aplicación
    os.chdir("/workspace/app-votantes")
    
    # Ejecutar Flask
    print("\n" + "="*50)
    print("🎯 ¡LISTO PARA PROBAR!")
    print("="*50)
    print("\nInstrucciones rápidas:")
    print("1. Ve a: http://127.0.0.1:5000")
    print("2. Inicia sesión como colaborador")
    print("3. Ve a 'Nuevo Votante'") 
    print("4. Haz clic en el botón GPS (📍)")
    print("5. ¡Prueba las 3 opciones de confirmación!")
    print("\n⚡ Presiona Ctrl+C para detener el servidor")
    print("="*50)
    
    # Importar y ejecutar la aplicación
    from app import app
    app.run(host='0.0.0.0', port=5000, debug=True)

def main():
    """Función principal"""
    # Mostrar instrucciones
    mostrar_instrucciones()
    
    # Verificar archivos
    if not verificar_archivos():
        print("\n❌ Algunos archivos no están presentes. Revisa la instalación.")
        return False
    
    print("\n✅ Todos los archivos están presentes")
    print("\n🎉 ¡La aplicación está lista!")
    
    respuesta = input("\n¿Deseas iniciar la aplicación ahora? (s/n): ").strip().lower()
    
    if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
        try:
            ejecutar_aplicacion()
        except KeyboardInterrupt:
            print("\n\n👋 Aplicación detenida por el usuario")
        except Exception as e:
            print(f"\n❌ Error al ejecutar la aplicación: {e}")
    else:
        print("\n📖 Para iniciar manualmente, ejecuta:")
        print("   cd /workspace/app-votantes && python app.py")
        print("\n📚 Documentación completa en: GPS_CONFIRMACION.md")
    
    return True

if __name__ == "__main__":
    main()