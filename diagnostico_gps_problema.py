#!/usr/bin/env python3
"""
Script de Diagnóstico: Problema GPS Auto-aplicación
===================================================

Este script analiza el código para identificar por qué el GPS se aplica
automáticamente cuando hay datos existentes pero no cuando están vacíos.
"""

import re
from pathlib import Path

def analizar_codigo_gps():
    """Analiza el código GPS para identificar el problema."""
    
    print("🔍 DIAGNÓSTICO: GPS Auto-aplicación Problem")
    print("=" * 50)
    
    # Archivos a analizar
    archivos = [
        "/workspace/app-votantes/templates/base.html",
        "/workspace/app-votantes/templates/nuevo_votante.html", 
        "/workspace/app-votantes/templates/editar_votante.html"
    ]
    
    for archivo in archivos:
        print(f"\n📁 Analizando: {Path(archivo).name}")
        print("-" * 40)
        
        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
            lineas = contenido.split('\n')
        
        # Buscar código relacionado con GPS
        patrones_problema = [
            r'geolocation\.getCurrentPosition',
            r'\.value\s*=\s*',
            r'navigator\.geolocation',
            r'obtenerUbicacionGPS',
            r'aplicarCoordenadasGPS',
            r'agregarBotonGPS',
            r'btn-gps'
        ]
        
        problemas_encontrados = []
        
        for i, linea in enumerate(lineas, 1):
            for patron in patrones_problema:
                if re.search(patron, linea, re.IGNORECASE):
                    problemas_encontrados.append(f"Línea {i}: {linea.strip()}")
        
        if problemas_encontrados:
            print(f"⚠️  Código GPS encontrado ({len(problemas_encontrados)} líneas):")
            for problema in problemas_encontrados:
                print(f"   {problema}")
        else:
            print("✅ No se encontró código GPS problemático")
    
    print("\n🎯 ANÁLISIS DEL PROBLEMA")
    print("=" * 50)
    
    # Análisis específico del problema reportado
    print("📝 PROBLEMA REPORTADO:")
    print("   - Con nombre ya cargado → GPS se aplica automáticamente")
    print("   - Sin nombre → GPS NO se aplica automáticamente")
    print("")
    
    print("🔍 POSIBLES CAUSAS IDENTIFICADAS:")
    print("")
    
    print("1. INICIALIZACIÓN AUTOMÁTICA EN NUEVO_VOTANTE:")
    print("   - Líneas 162-170: geolocation.getCurrentPosition automático")
    print("   - Esto podría estar causando actualización no deseada")
    print("")
    
    print("2. CÓDIGO DUPLICADO EN MANEJO DE CAMPOS:")
    print("   - base.html: aplicarCoordenadasGPS() (CORRECTO)")
    print("   - editar_votante.html: actualización directa (CORRECTO para manual)")
    print("   - nuevo_votante.html: actualización directa (CORRECTO para manual)")
    print("")
    
    print("3. DIFERENCIAS ENTRE FORMULARIOS:")
    print("   - nuevo_votante.html: geolocation automático al cargar")
    print("   - editar_votante.html: centra en datos existentes")
    print("")
    
    print("🛠️  SOLUCIÓN RECOMENDADA:")
    print("=" * 30)
    print("1. Eliminar geolocation automático en nuevo_votante.html")
    print("2. Verificar que solo se active GPS con botón explícito")
    print("3. Asegurar confirmación requerida en todos los casos")
    
    print("\n✅ DIAGNÓSTICO COMPLETADO")
    print("El problema más probable es la inicialización automática")
    print("en nuevo_votante.html que interfiere con el flujo GPS.")

if __name__ == "__main__":
    analizar_codigo_gps()