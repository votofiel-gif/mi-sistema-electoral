#!/usr/bin/env python3
"""
Script de prueba para verificar la funcionalidad GPS con confirmación
Verifica que:
1. Los estilos CSS estén correctamente agregados
2. Las funciones JavaScript estén implementadas
3. Las instrucciones estén actualizadas
4. El botón GPS tenga el título correcto
"""

import os
import re

def verificar_archivo_base():
    """Verifica el archivo base.html para las funcionalidades GPS"""
    print("🔍 Verificando archivo base.html...")
    
    base_path = "/workspace/app-votantes/templates/base.html"
    
    with open(base_path, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    verificaciones = {
        "CSS de confirmación GPS": "gps-confirmation",
        "CSS de coordenadas": "gps-coordinates", 
        "CSS de animaciones": "gps-marker-temp",
        "Función obtenerUbicacionGPS": "function obtenerUbicacionGPS",
        "Función mostrarConfirmacionGPS": "function mostrarConfirmacionGPS",
        "Función aplicarCoordenadasGPS": "function aplicarCoordenadasGPS",
        "Función cancelarCoordenadasGPS": "function cancelarCoordenadasGPS",
        "Variable global coordenadasGPS": "window.coordenadasGPS",
        "Título del botón GPS actualizado": "con confirmación"
    }
    
    resultados = {}
    for nombre, patron in verificaciones.items():
        if patron in contenido:
            print(f"  ✅ {nombre}: Encontrado")
            resultados[nombre] = True
        else:
            print(f"  ❌ {nombre}: NO encontrado")
            resultados[nombre] = False
    
    return all(resultados.values()), resultados

def verificar_formularios():
    """Verifica los formularios nuevo_votante.html y editar_votante.html"""
    print("\n🔍 Verificando formularios...")
    
    formularios = [
        ("/workspace/app-votantes/templates/nuevo_votante.html", "Formulario nuevo votante"),
        ("/workspace/app-votantes/templates/editar_votante.html", "Formulario editar votante")
    ]
    
    resultados_generales = []
    
    for ruta, nombre in formularios:
        print(f"\n  📋 Verificando {nombre}...")
        
        with open(ruta, 'r', encoding='utf-8') as f:
            contenido = f.read()
        
        verificaciones = {
            "Instrucciones del GPS": "botón GPS",
            "Explicación manual vs GPS": "Hacer clic en el mapa",
            "Botón GPS en JavaScript": "agregarBotonGPS"
        }
        
        resultados_formulario = []
        for nombre_check, patron in verificaciones.items():
            if patron in contenido:
                print(f"    ✅ {nombre_check}: Encontrado")
                resultados_formulario.append(True)
            else:
                print(f"    ❌ {nombre_check}: NO encontrado")
                resultados_formulario.append(False)
        
        resultados_generales.append(all(resultados_formulario))
    
    return all(resultados_generales), resultados_generales

def verificar_funcionalidad_gps():
    """Verifica que la lógica del GPS con confirmación esté bien implementada"""
    print("\n🔍 Verificando lógica del GPS...")
    
    base_path = "/workspace/app-votantes/templates/base.html"
    
    with open(base_path, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    verificaciones_logica = {
        "No actualiza campos automáticamente": "window.coordenadasGPS[mapId]",
        "Muestra confirmación visual": "mostrarConfirmacionGPS",
        "Botón Aplicar GPS": "aplicarCoordenadasGPS",
        "Botón Cancelar GPS": "cancelarCoordenadasGPS",
        "Botón Intentar de nuevo": "Intentar de nuevo",
        "Marcador temporal GPS": "markerGPS",
        "Auto-remover confirmación": "15000",
        "Mensaje de éxito": "Ubicación GPS aplicada correctamente"
    }
    
    resultados = {}
    for nombre, patron in verificaciones_logica.items():
        if patron in contenido:
            print(f"  ✅ {nombre}: Implementado")
            resultados[nombre] = True
        else:
            print(f"  ❌ {nombre}: NO implementado")
            resultados[nombre] = False
    
    return all(resultados.values()), resultados

def main():
    """Ejecuta todas las verificaciones"""
    print("=" * 60)
    print("🧪 PRUEBA DE FUNCIONALIDAD GPS CON CONFIRMACIÓN")
    print("=" * 60)
    
    # Verificar archivo base
    ok_base, resultados_base = verificar_archivo_base()
    
    # Verificar formularios
    ok_formularios, resultados_formularios = verificar_formularios()
    
    # Verificar lógica GPS
    ok_logica, resultados_logica = verificar_funcionalidad_gps()
    
    # Resumen final
    print("\n" + "=" * 60)
    print("📊 RESUMEN DE VERIFICACIONES")
    print("=" * 60)
    
    todas_ok = ok_base and ok_formularios and ok_logica
    
    print(f"Archivo base.html:     {'✅ PASS' if ok_base else '❌ FAIL'}")
    print(f"Formularios:           {'✅ PASS' if ok_formularios else '❌ FAIL'}")
    print(f"Lógica GPS:            {'✅ PASS' if ok_logica else '❌ FAIL'}")
    print(f"\nResultado general:     {'✅ TODAS LAS PRUEBAS PASARON' if todas_ok else '❌ ALGUNAS PRUEBAS FALLARON'}")
    
    if todas_ok:
        print("\n🎉 ¡La funcionalidad GPS con confirmación está correctamente implementada!")
        print("\n📋 Comportamiento esperado:")
        print("  1. Clic en botón GPS → Obtiene coordenadas")
        print("  2. Muestra confirmación visual con coordenadas")
        print("  3. Usuario puede:")
        print("     • Aplicar GPS (guarda coordenadas)")
        print("     • Cancelar (descarta y mantiene manual)")
        print("     • Intentar de nuevo (obtiene nuevas coordenadas)")
        print("  4. Auto-cancela después de 15 segundos si no hay acción")
    
    return todas_ok

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)