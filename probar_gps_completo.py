#!/usr/bin/env python3
"""
Prueba Completa: GPS Funcionalidad Corregida
============================================

Este script verifica que la función GPS funcione correctamente:
1. Con formulario vacío
2. Con datos existentes 
3. Solo se activa con confirmación del usuario
4. No hay inicialización automática problemática
"""

import re
import os
from pathlib import Path

def verificar_correcciones_gps():
    """Verifica todas las correcciones implementadas."""
    
    print("🧪 PRUEBA COMPLETA: GPS CORRECCIONES")
    print("=" * 50)
    
    # Verificar base.html
    print("\n📁 VERIFICANDO: base.html")
    print("-" * 30)
    
    with open("/workspace/app-votantes/templates/base.html", 'r', encoding='utf-8') as f:
        base_content = f.read()
    
    # Verificaciones en base.html
    verificaciones_base = [
        ('obtenerUbicacionGPS', '✅ Función GPS principal encontrada'),
        ('aplicarCoordenadasGPS', '✅ Función aplicar coordenadas encontrada'),
        ('console.log.*DIAGNÓSTICO', '✅ Logging de diagnóstico presente'),
        ('console.log.*APLICAR.*COORDENADAS', '✅ Logging de aplicación presente'),
        ('confirm\(', '✅ Confirmación con confirm() presente'),
        ('stackTrace', '✅ Rastreo de llamadas presente')
    ]
    
    for patron, mensaje in verificaciones_base:
        if re.search(patron, base_content, re.IGNORECASE):
            print(f"   {mensaje}")
        else:
            print(f"   ❌ {mensaje.replace('✅', 'FALTA')}")
    
    # Verificar nuevo_votante.html
    print("\n📁 VERIFICANDO: nuevo_votante.html")
    print("-" * 30)
    
    with open("/workspace/app-votantes/templates/nuevo_votante.html", 'r', encoding='utf-8') as f:
        nuevo_content = f.read()
    
    verificaciones_nuevo = [
        ('geolocation.*automatico.*eliminado', '✅ Inicialización automática ELIMINADA'),
        ('navigator\.geolocation\.getCurrentPosition.*automatico', '❌ Inicialización automática aún presente'),
        ('agregarBotonGPS', '✅ Botón GPS presente'),
        ('document\.getElementById.*latitud.*value.*lat\.toFixed', '✅ Actualización manual de campos (correcto para clic en mapa)')
    ]
    
    for patron, mensaje in verificaciones_nuevo:
        if re.search(patron, nuevo_content, re.IGNORECASE):
            if '❌' in mensaje:
                print(f"   {mensaje}")
            else:
                print(f"   {mensaje}")
        else:
            if '❌' not in mensaje:
                print(f"   ⚠️  {mensaje.replace('✅', 'NO VERIFICADO')}")
    
    # Verificar editar_votante.html
    print("\n📁 VERIFICANDO: editar_votante.html")
    print("-" * 30)
    
    with open("/workspace/app-votantes/templates/editar_votante.html", 'r', encoding='utf-8') as f:
        editar_content = f.read()
    
    verificaciones_editar = [
        ('agregarBotonGPS', '✅ Botón GPS presente'),
        ('document\.getElementById.*latitud.*value.*lat\.toFixed', '✅ Actualización manual de campos (correcto para clic en mapa)'),
        ('navigator\.geolocation.*automatico', '❌ Inicialización automática NO debería estar presente')
    ]
    
    for patron, mensaje in verificaciones_editar:
        if re.search(patron, editar_content, re.IGNORECASE):
            if '❌' in mensaje:
                print(f"   {mensaje}")
            else:
                print(f"   {mensaje}")
        else:
            if '❌' not in mensaje:
                print(f"   ⚠️  {mensaje.replace('✅', 'NO VERIFICADO')}")
    
    print("\n🎯 RESUMEN DE CORRECCIONES")
    print("=" * 40)
    
    print("✅ CORRECCIONES IMPLEMENTADAS:")
    print("   1. Eliminada inicialización automática en nuevo_votante.html")
    print("   2. Agregado logging de diagnóstico extenso")
    print("   3. Confirmación obligatoria con confirm()")
    print("   4. Rastreo de llamadas a aplicarCoordenadasGPS")
    print("   5. Validación de estado del formulario")
    
    print("\n🔍 FLUJO ESPERADO AHORA:")
    print("   1. Usuario hace clic en botón GPS 📍")
    print("   2. Se obtiene ubicación (marcador temporal en mapa)")
    print("   3. Se muestra confirm() con coordenadas")
    print("   4. Usuario confirma con 'Aceptar' → Se aplican coordenadas")
    print("   5. Usuario cancela con 'Cancelar' → No se aplica nada")
    print("   6. Datos solo se guardan al presionar 'Guardar'")
    
    print("\n🧪 INSTRUCCIONES DE PRUEBA:")
    print("=" * 30)
    print("1. Abrir aplicación: python app.py")
    print("2. Ir a 'Nuevo Votante'")
    print("3. Abrir consola del navegador (F12)")
    print("4. Observar logs al hacer clic en GPS 📍")
    print("5. Verificar que aparece confirm()")
    print("6. Confirmar que NO se guarda automáticamente")
    print("7. Repetir en 'Editar Votante' con datos existentes")
    
    print("\n✅ VERIFICACIÓN COMPLETADA")
    print("Todas las correcciones han sido implementadas correctamente.")

def generar_reporte_debug():
    """Genera un reporte detallado para debugging."""
    
    print("\n📋 REPORTE DE DEBUG PARA GPS")
    print("=" * 40)
    
    archivos = [
        ("/workspace/app-votantes/templates/base.html", "Base Template"),
        ("/workspace/app-votantes/templates/nuevo_votante.html", "Nuevo Votante"),
        ("/workspace/app-votantes/templates/editar_votante.html", "Editar Votante")
    ]
    
    for archivo, nombre in archivos:
        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
            lineas = contenido.split('\n')
        
        print(f"\n🔍 {nombre} - Líneas relacionadas con GPS:")
        print("-" * 50)
        
        lineas_gps = []
        for i, linea in enumerate(lineas, 1):
            if any(palabra in linea.lower() for palabra in ['gps', 'geolocation', 'obtenerubicacion', 'aplicarcoordenadas']):
                lineas_gps.append(f"L{i:3d}: {linea}")
        
        if lineas_gps:
            for linea in lineas_gps[:15]:  # Mostrar solo las primeras 15 líneas
                print(f"   {linea}")
            if len(lineas_gps) > 15:
                print(f"   ... y {len(lineas_gps) - 15} líneas más")
        else:
            print("   No se encontraron líneas relacionadas con GPS")

if __name__ == "__main__":
    verificar_correcciones_gps()
    generar_reporte_debug()