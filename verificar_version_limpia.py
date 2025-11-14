#!/usr/bin/env python3
"""
Script para verificar que la versión limpia sin banner y con mensajes reducidos esté implementada
"""

def verificar_version_limpia():
    """Verifica que la versión limpia esté implementada"""
    print("🔍 VERIFICANDO VERSIÓN LIMPIA GPS")
    print("=" * 50)
    
    try:
        with open('templates/base.html', 'r', encoding='utf-8') as f:
            contenido = f.read()
            
        # Verificaciones
        verificaciones = [
            ("Banner visual removido", "Sistema GPS Anti-Auto-Guardo ACTIVADO" not in contenido),
            ("Versión actualizada", "2025-11-14-04-44" in contenido),
            ("Mensajes de GPS simplificados", "📱 VERSIÓN LIMPIA" in contenido),
            ("Confirmación GPS simplificada", "GPS confirmado por usuario" in contenido),
            ("Aplicación de coordenadas simplificada", "📍 Aplicando coordenadas GPS" in contenido),
            ("Indicador visual removido", "Indicador visual de protección activa" not in contenido),
            ("Banner removido", "const indicador = document.createElement('div')" not in contenido),
        ]
        
        exitos = 0
        for descripcion, resultado in verificaciones:
            if resultado:
                print(f"✅ {descripcion}: OK")
                exitos += 1
            else:
                print(f"❌ {descripcion}: FALTA")
        
        print("\n" + "=" * 50)
        print(f"📊 RESULTADO: {exitos}/{len(verificaciones)} verificaciones")
        
        if exitos == len(verificaciones):
            print("\n🎉 ¡VERSIÓN LIMPIA IMPLEMENTADA CORRECTAMENTE!")
            print("\n📋 CAMBIOS REALIZADOS:")
            print("1. 🗑️ Banner visual '🛡️ Sistema GPS Anti-Auto-Guardo ACTIVADO' REMOVIDO")
            print("2. 🔇 Mensajes de consola reducidos significativamente")
            print("3. 📱 Versión actualizada a '2025-11-14-04-44'")
            print("4. ✅ Confirmación GPS simplificada a un solo mensaje")
            print("5. 📍 Aplicación de coordenadas simplificada")
            
            print("\n🚀 INSTRUCCIONES:")
            print("1. Reinicia: python app.py")
            print("2. Abre navegador en incógnito")
            print("3. Ve a 'Nuevo Votante'")
            print("4. Prueba GPS - ahora debe mostrar:")
            print("   - Un solo mensaje de confirmación")
            print("   - Sin banner visual en la esquina")
            print("   - Consola mucho más limpia")
        else:
            print("\n⚠️ FALTAN VERIFICACIONES")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    verificar_version_limpia()
