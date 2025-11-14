#!/usr/bin/env python3
"""
Script para probar que las fotos y cédulas funcionan correctamente
"""

import os
import sqlite3

def probar_fotos_y_cedulas():
    """Prueba que las fotos se vean correctamente y que el campo cédula esté presente"""
    
    print("🔍 Probando funcionalidad de fotos y cédulas...")
    
    # Verificar que la carpeta uploads existe
    print("📁 Verificando carpeta uploads...")
    if os.path.exists('uploads'):
        print("   ✅ Carpeta uploads existe")
        archivos = os.listdir('uploads')
        print(f"   📄 Archivos en uploads: {len(archivos)}")
        if archivos:
            print("   📋 Primeros archivos:")
            for i, archivo in enumerate(archivos[:3]):
                print(f"      - {archivo}")
    else:
        print("   ⚠️ Carpeta uploads no existe")
    
    # Verificar base de datos
    print("\n💾 Verificando base de datos...")
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Verificar estructura de la tabla
    cursor.execute("PRAGMA table_info(votantes)")
    columnas = cursor.fetchall()
    print("   📋 Columnas en la tabla votantes:")
    for col in columnas:
        print(f"      - {col[1]} ({col[2]})")
    
    # Verificar datos con cédulas
    print("\n👥 Verificando votantes con cédulas:")
    cursor.execute("SELECT id, nombre_completo, numero_cedula, foto FROM votantes ORDER BY id LIMIT 5")
    votantes = cursor.fetchall()
    
    for votante in votantes:
        id_votante, nombre, cedula, foto = votante
        estado_foto = "✅" if foto else "❌"
        estado_cedula = "✅" if cedula else "❌"
        print(f"   ID {id_votante}: {nombre}")
        print(f"      Cédula: {cedula} {estado_cedula}")
        print(f"      Foto: {foto} {estado_foto}")
    
    # Verificar que las rutas de fotos son correctas
    print("\n🖼️ Verificando rutas de fotos...")
    for votante in votantes[:3]:  # Solo los primeros 3
        id_votante, nombre, cedula, foto = votante
        if foto:
            ruta_completa = os.path.join('uploads', foto)
            existe = "✅" if os.path.exists(ruta_completa) else "❌"
            print(f"   {nombre}: {ruta_completa} {existe}")
    
    conn.close()
    print("\n✅ Prueba completada")

if __name__ == "__main__":
    probar_fotos_y_cedulas()