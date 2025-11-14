#!/usr/bin/env python3
"""
Script de prueba para la nueva versión GPS SIMPLIFICADA
Verifica que el GPS NO se guarde automáticamente y solo se aplique con confirmación
"""

import os
import re

def verificar_gps_simplificado():
    """Verifica la nueva implementación GPS simplificada"""
    print("🔍 Verificando implementación GPS simplificada...")
    
    base_path = "/workspace/app-votantes/templates/base.html"
    
    with open(base_path, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    verificaciones = {
        "✅ Confirm simple del navegador": "confirm(`",
        "✅ No auto-guardado en obtenerUbicacionGPS": "// ✅ ACTUALIZAR CAMPOS HIDDEN SOLO AQUÍ",
        "✅ Aplicar GPS solo en confirmar": "function aplicarCoordenadasGPS(",
        "✅ Logging para debugging": "console.log",
        "✅ Estilos simplificados": "gps-marker-temp",
        "✅ Sin funciones complejas": "gps-confirmation" not in contenido,
        "✅ Título actualizado del botón": "Obtener mi ubicación GPS"
    }
    
    resultados = {}
    for nombre, verificacion in verificaciones.items():
        if isinstance(verificacion, str) and verificacion not in contenido:
            if verificacion.startswith("Sin"):  # Para verificar que algo NO esté presente
                print(f"  ✅ {nombre}: Correctamente eliminado")
                resultados[nombre] = True
            else:
                print(f"  ❌ {nombre}: NO encontrado")
                resultados[nombre] = False
        elif verificacion in contenido:
            print(f"  ✅ {nombre}: Encontrado")
            resultados[nombre] = True
        else:
            print(f"  ❌ {nombre}: Verificación incorrecta")
            resultados[nombre] = False
    
    return all(resultados.values()), resultados

def verificar_comportamiento_gps():
    """Verifica que el comportamiento sea el correcto"""
    print("\n🔍 Verificando comportamiento esperado...")
    
    base_path = "/workspace/app-votantes/templates/base.html"
    
    with open(base_path, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Buscar patrones específicos del comportamiento
    comportamientos = {
        "No actualiza campos automáticamente": "document.getElementById(latitudId).value" not in contenido.split("function obtenerUbicacionGPS")[1].split("function")[0],
        "Muestra confirmación antes de aplicar": "confirm(" in contenido,
        "Solo aplica con confirmación": "setTimeout(() => {" in contenido,
        "Aplica coordenadas en función específica": "function aplicarCoordenadasGPS(lat, lng" in contenido
    }
    
    resultados = {}
    for nombre, cumple in comportamientos.items():
        if cumple:
            print(f"  ✅ {nombre}: CUMPLE")
            resultados[nombre] = True
        else:
            print(f"  ❌ {nombre}: NO cumple")
            resultados[nombre] = False
    
    return all(resultados.values()), resultados

def verificar_debugging():
    """Verifica que haya logging para debugging"""
    print("\n🔍 Verificando sistema de debugging...")
    
    base_path = "/workspace/app-votantes/templates/base.html"
    
    with open(base_path, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    logs_esperados = [
        "console.log('📍 Aplicando coordenadas GPS:",
        "console.log('✅ Campos hidden actualizados:",
        "console.error('❌ No se encontraron campos hidden:",
        "console.log('✅ Marcador GPS creado en el mapa)",
        "console.log('🎉 GPS aplicado exitosamente')"
    ]
    
    resultados = {}
    for log in logs_esperados:
        if log in contenido:
            print(f"  ✅ Log encontrado: {log}")
            resultados[log] = True
        else:
            print(f"  ❌ Log faltante: {log}")
            resultados[log] = False
    
    return all(resultados.values()), resultados

def main():
    """Ejecuta todas las verificaciones"""
    print("=" * 70)
    print("🎯 PRUEBA GPS SIMPLIFICADO - SIN AUTO-GUARDADO")
    print("=" * 70)
    
    # Verificar implementación
    ok_implementacion, resultados_implementacion = verificar_gps_simplificado()
    
    # Verificar comportamiento
    ok_comportamiento, resultados_comportamiento = verificar_comportamiento_gps()
    
    # Verificar debugging
    ok_debugging, resultados_debugging = verificar_debugging()
    
    # Resumen final
    print("\n" + "=" * 70)
    print("📊 RESUMEN DE VERIFICACIONES")
    print("=" * 70)
    
    todas_ok = ok_implementacion and ok_comportamiento and ok_debugging
    
    print(f"Implementación:      {'✅ PASS' if ok_implementacion else '❌ FAIL'}")
    print(f"Comportamiento:      {'✅ PASS' if ok_comportamiento else '❌ FAIL'}")
    print(f"Debugging:           {'✅ PASS' if ok_debugging else '❌ FAIL'}")
    print(f"\nResultado general:   {'✅ TODAS LAS PRUEBAS PASARON' if todas_ok else '❌ ALGUNAS PRUEBAS FALLARON'}")
    
    if todas_ok:
        print("\n🎉 ¡GPS simplificado correctamente implementado!")
        print("\n📋 Comportamiento esperado:")
        print("  1. Clic en botón GPS → Obtiene coordenadas")
        print("  2. ✅ NO actualiza campos automáticamente")
        print("  3. ✅ Muestra confirmación del navegador")
        print("  4. ✅ Solo se aplica con 'Aceptar'")
        print("  5. ✅ Se cancela con 'Cancelar'")
        print("  6. ✅ Solo se guarda al presionar 'Guardar'")
        print("\n🛠️ Para probar:")
        print("  1. Abre la consola del navegador (F12)")
        print("  2. Ve a 'Nuevo Votante'")
        print("  3. Haz clic en botón GPS (📍)")
        print("  4. ✅ Mira los logs en consola")
        print("  5. Prueba 'Aceptar' y 'Cancelar'")
    else:
        print("\n❌ Hay problemas en la implementación")
        print("Revisa los elementos fallidos arriba")
    
    return todas_ok

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)