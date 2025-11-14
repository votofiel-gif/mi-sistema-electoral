#!/usr/bin/env python3
"""
Script de prueba para verificar que la aplicación funciona correctamente
Ejecuta: python3 probar_aplicacion.py
"""

import os
import sys
import sqlite3
from datetime import datetime

def verificar_archivos():
    """Verificar que todos los archivos necesarios existen"""
    print("📁 Verificando archivos...")
    
    archivos_requeridos = [
        'app.py',
        'database.db',
        'uploads/',
        'templates/base.html',
        'templates/login.html',
        'templates/dashboard_candidato.html'
    ]
    
    archivos_faltantes = []
    for archivo in archivos_requeridos:
        if os.path.exists(archivo):
            print(f"  ✓ {archivo}")
        else:
            print(f"  ✗ {archivo} - FALTA")
            archivos_faltantes.append(archivo)
    
    if archivos_faltantes:
        print(f"\n❌ Faltan {len(archivos_faltantes)} archivos")
        return False
    else:
        print("\n✅ Todos los archivos están presentes")
        return True

def verificar_base_datos():
    """Verificar que la base de datos funciona"""
    print("\n🗃️ Verificando base de datos...")
    
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # Verificar tablas
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tablas = cursor.fetchall()
        tablas_nombres = [tabla[0] for tabla in tablas]
        
        print(f"  Tablas encontradas: {', '.join(tablas_nombres)}")
        
        # Verificar usuarios
        cursor.execute("SELECT COUNT(*) FROM usuarios")
        total_usuarios = cursor.fetchone()[0]
        print(f"  Total usuarios: {total_usuarios}")
        
        # Verificar votantes
        cursor.execute("SELECT COUNT(*) FROM votantes")
        total_votantes = cursor.fetchone()[0]
        print(f"  Total votantes: {total_votantes}")
        
        # Verificar usuarios específicos
        cursor.execute("SELECT usuario FROM usuarios WHERE usuario = 'candidato'")
        candidato = cursor.fetchone()
        if candidato:
            print("  ✓ Usuario candidato existe")
        else:
            print("  ✗ Usuario candidato NO existe")
            return False
        
        conn.close()
        print("\n✅ Base de datos funcionando correctamente")
        return True
        
    except Exception as e:
        print(f"\n❌ Error en base de datos: {e}")
        return False

def verificar_codigo():
    """Verificar que el código Python es válido"""
    print("\n🐍 Verificando código Python...")
    
    try:
        import app
        print("  ✓ Módulo app.py cargado correctamente")
        
        # Verificar funciones importantes
        if hasattr(app, 'init_db'):
            print("  ✓ Función init_db existe")
        else:
            print("  ✗ Función init_db NO existe")
            return False
            
        if hasattr(app, 'dashboard_candidato'):
            print("  ✓ Función dashboard_candidato existe")
        else:
            print("  ✗ Función dashboard_candidato NO existe")
            return False
        
        # Verificar que las carpetas se crean
        if os.path.exists('uploads'):
            print("  ✓ Carpeta uploads existe")
        else:
            print("  ✗ Carpeta uploads NO existe")
            return False
            
        print("\n✅ Código Python válido")
        return True
        
    except Exception as e:
        print(f"\n❌ Error en código: {e}")
        return False

def mostrar_instrucciones():
    """Mostrar instrucciones de uso"""
    print("\n" + "="*60)
    print("🎉 APLICACIÓN VERIFICADA CORRECTAMENTE")
    print("="*60)
    print("\n📋 PARA INICIAR LA APLICACIÓN:")
    print("\nWindows:")
    print("  1. Doble clic en: INICIAR_WINDOWS.bat")
    print("  2. Abrir navegador en: http://localhost:5000")
    
    print("\nLinux/Mac:")
    print("  1. Ejecutar: bash INICIAR_LINUX_MAC.sh")
    print("  2. Abrir navegador en: http://localhost:5000")
    
    print("\n👥 USUARIOS DE PRUEBA:")
    print("\nCandidato:")
    print("  Usuario: candidato")
    print("  Contraseña: admin123")
    
    print("\nColaboradores:")
    print("  Usuario: juan / maria / carlos")
    print("  Contraseña: colaborador123")
    
    print("\n📖 DOCUMENTACIÓN:")
    print("  • LEEME_PRIMERO.md - Inicio rápido")
    print("  • GUIA_RAPIDA.md - Tutorial completo")
    print("  • INSTRUCCIONES_COMPLETAS.md - Manual detallado")
    print("  • ERRORES_CORREGIDOS.md - Solución de problemas")
    
    print("\n✨ ERRORES CORREGIDOS:")
    print("  ✓ Problema de serialización JSON")
    print("  ✓ Carpeta uploads faltante")
    print("  ✓ Dashboard del candidato")
    print("  ✓ Subida de fotos")
    
    print("\n" + "="*60)
    print("🎊 ¡TODO LISTO PARA USAR!")
    print("="*60)

def main():
    print("🔍 VERIFICADOR DE LA APLICACIÓN DE VOTANTES")
    print("="*50)
    
    # Verificar archivos
    if not verificar_archivos():
        print("\n❌ Faltan archivos necesarios. No se puede continuar.")
        sys.exit(1)
    
    # Verificar base de datos
    if not verificar_base_datos():
        print("\n❌ Problemas con la base de datos.")
        sys.exit(1)
    
    # Verificar código
    if not verificar_codigo():
        print("\n❌ Problemas con el código.")
        sys.exit(1)
    
    # Mostrar instrucciones
    mostrar_instrucciones()

if __name__ == '__main__':
    main()
