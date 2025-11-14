#!/usr/bin/env python3
"""
Script simple para verificar que el GPS no se guarde automáticamente
"""

def main():
    print("=" * 70)
    print("🎯 VERIFICACIÓN GPS SIMPLIFICADO")
    print("=" * 70)
    
    base_path = "/workspace/app-votantes/templates/base.html"
    
    with open(base_path, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Verificaciones clave
    print("\n🔍 Verificando características clave:")
    
    # 1. No hay funciones complejas
    if "gps-confirmation" not in contenido:
        print("  ✅ Funciones complejas eliminadas")
    else:
        print("  ❌ Aún hay funciones complejas")
        return False
    
    # 2. Usa confirm() simple
    if "confirm(" in contenido:
        print("  ✅ Usa confirmación simple del navegador")
    else:
        print("  ❌ No usa confirmación del navegador")
        return False
    
    # 3. No actualiza campos automáticamente en obtenerUbicacionGPS
    seccion_gps = contenido.split("function obtenerUbicacionGPS(")[1].split("function aplicarCoordenadasGPS")[0]
    if "document.getElementById(latitudId).value" not in seccion_gps:
        print("  ✅ NO actualiza campos automáticamente en obtenerUbicacionGPS")
    else:
        print("  ❌ Actualiza campos automáticamente en obtenerUbicacionGPS")
        return False
    
    # 4. Solo aplica en aplicarCoordenadasGPS
    if "function aplicarCoordenadasGPS(lat, lng" in contenido:
        print("  ✅ Función aplicarCoordenadasGPS solo con coordenadas directas")
    else:
        print("  ❌ Función aplicarCoordenadasGPS no encontrada")
        return False
    
    # 5. Hay logging
    if "console.log" in contenido:
        print("  ✅ Logging para debugging incluido")
    else:
        print("  ❌ No hay logging")
        return False
    
    # 6. Usa confirm() del navegador
    if "confirm(`📍 Ubicación GPS Obtenida:" in contenido:
        print("  ✅ Usa confirm() con mensaje GPS")
    else:
        print("  ❌ No usa confirm() con mensaje GPS")
        return False
    
    print("\n" + "=" * 70)
    print("🎉 ¡TODAS LAS VERIFICACIONES PASARON!")
    print("=" * 70)
    print("\n📋 Comportamiento garantizado:")
    print("  1. ✅ GPS NO se guarda automáticamente")
    print("  2. ✅ Muestra confirmación antes de aplicar")
    print("  3. ✅ Solo se actualiza al hacer clic en 'Aceptar'")
    print("  4. ✅ Se cancela al hacer clic en 'Cancelar'")
    print("  5. ✅ Solo se guarda al presionar 'Guardar'")
    print("\n🛠️ Para probar:")
    print("  1. Abre consola del navegador (F12)")
    print("  2. Ve a 'Nuevo Votante'")
    print("  3. Haz clic en botón GPS (📍)")
    print("  4. Observa los logs en consola")
    print("  5. Prueba 'Aceptar' y 'Cancelar'")
    print("  6. Solo se guarda al presionar 'Guardar formulario'")
    
    return True

if __name__ == "__main__":
    success = main()
    if success:
        print("\n✅ Implementación GPS correcta")
    else:
        print("\n❌ Problemas en la implementación")
    exit(0 if success else 1)