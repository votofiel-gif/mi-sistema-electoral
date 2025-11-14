#!/usr/bin/env python3
"""
Script para verificar que la solución GPS final esté implementada correctamente
"""

import os

def verificar_archivo(archivo, texto_busqueda, descripcion):
    """Verifica que un texto específico esté en un archivo"""
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
            if texto_busqueda in contenido:
                print(f"✅ {descripcion}: ENCONTRADO")
                return True
            else:
                print(f"❌ {descripcion}: NO ENCONTRADO")
                return False
    except Exception as e:
        print(f"❌ Error leyendo {archivo}: {e}")
        return False

def main():
    print("🔍 VERIFICANDO SOLUCIÓN GPS ANTI-AUTO-GUARDADO")
    print("=" * 60)
    
    # Archivos a verificar
    base_html = "templates/base.html"
    nuevo_html = "templates/nuevo_votante.html"
    editar_html = "templates/editar_votante.html"
    
    # Verificaciones
    verificaciones = [
        (base_html, "e.stopPropagation()", "Protección anti-propagación en base.html"),
        (base_html, "📍 BOTÓN GPS CLICKEADO", "Log de click GPS en base.html"),
        (base_html, "btnGps.addEventListener('click'", "Event listener GPS en base.html"),
        
        (nuevo_html, "let bloqueandoGPS = false", "Flag bloqueandoGPS en nuevo_votante.html"),
        (nuevo_html, "if (bloqueandoGPS)", "Verificación bloqueandoGPS en nuevo_votante.html"),
        (nuevo_html, "bloqueandoGPS = true", "Activación bloqueandoGPS en nuevo_votante.html"),
        (nuevo_html, "window.obtenerUbicacionGPS", "Función obtenerUbicacionGPS en nuevo_votante.html"),
        
        (editar_html, "let bloqueandoGPS = false", "Flag bloqueandoGPS en editar_votante.html"),
        (editar_html, "if (bloqueandoGPS)", "Verificación bloqueandoGPS en editar_votante.html"),
        (editar_html, "bloqueandoGPS = true", "Activación bloqueandoGPS en editar_votante.html"),
        (editar_html, "window.obtenerUbicacionGPS", "Función obtenerUbicacionGPS en editar_votante.html"),
    ]
    
    exitos = 0
    total = len(verificaciones)
    
    for archivo, texto, descripcion in verificaciones:
        if verificar_archivo(archivo, texto, descripcion):
            exitos += 1
        print()
    
    print("=" * 60)
    print(f"📊 RESULTADO: {exitos}/{total} verificaciones exitosas")
    
    if exitos == total:
        print("🎉 ¡SOLUCIÓN IMPLEMENTADA CORRECTAMENTE!")
        print("\n📋 PASOS PARA PROBAR:")
        print("1. 🔄 Reinicia la aplicación: python app.py")
        print("2. 🌐 Abre navegador en modo incógnito")
        print("3. 📍 Ve a 'Nuevo Votante'")
        print("4. ⌨️  Abre consola (F12)")
        print("5. 📍 Haz click en botón GPS")
        print("6. ✅ Verifica que aparezcan estos logs:")
        print("   - '📍 BOTÓN GPS CLICKEADO - EVENT STOP PROPAGATION'")
        print("   - '🚫 ACTIVANDO BLOQUEO ANTI-CONFLICTO GPS'")
        print("7. 🛑 Confirma que NO se guarda automáticamente")
    else:
        print("⚠️  FALTAN VERIFICACIONES - Revisa la implementación")
    
    print("\n🔧 Si el problema persiste:")
    print("- Asegúrate de hacer HARD REFRESH (Ctrl+F5)")
    print("- Usa modo incógnito para evitar cache")
    print("- Reinicia el servidor Python completamente")

if __name__ == "__main__":
    main()
