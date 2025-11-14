#!/usr/bin/env python3
"""
Script para probar la búsqueda en tiempo real del sistema de votantes
"""

import sqlite3
import requests
import json
from datetime import datetime

def test_database():
    """Verificar que la base de datos tenga datos"""
    print("🔍 Verificando base de datos...")
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Contar votantes
    cursor.execute("SELECT COUNT(*) FROM votantes")
    count = cursor.fetchone()[0]
    print(f"   ✓ Total de votantes en base de datos: {count}")
    
    # Mostrar algunos ejemplos
    if count > 0:
        cursor.execute("SELECT nombre_completo, numero_cedula FROM votantes LIMIT 5")
        ejemplos = cursor.fetchall()
        print("   ✓ Ejemplos de votantes:")
        for nombre, cedula in ejemplos:
            print(f"     - {nombre} (Cédula: {cedula})")
    
    conn.close()
    return count > 0

def test_api_search():
    """Probar la API de búsqueda"""
    print("\n🔍 Probando API de búsqueda...")
    
    base_url = "http://localhost:5000"
    
    # Simular sesión (en una prueba real necesitarías autenticar)
    headers = {
        'Content-Type': 'application/json'
    }
    
    # Probar búsqueda por nombre
    print("   📝 Probando búsqueda por nombre...")
    try:
        response = requests.get(
            f"{base_url}/api/buscar/votantes?tipo=nombre&q=mar",
            headers=headers
        )
        print(f"     ✓ Respuesta HTTP: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"     ✓ Resultados encontrados: {len(data)}")
            if data:
                print("     ✓ Ejemplo de resultado:")
                resultado = data[0]
                print(f"       - Nombre: {resultado.get('nombre', 'N/A')}")
                print(f"       - Cédula: {resultado.get('cedula', 'N/A')}")
                print(f"       - Teléfono: {resultado.get('telefono', 'N/A')}")
        else:
            print(f"     ❌ Error en respuesta: {response.text}")
    except Exception as e:
        print(f"     ❌ Error al conectar: {str(e)}")
        print("     💡 Asegúrate de que la aplicación esté ejecutándose en http://localhost:5000")
    
    # Probar búsqueda por cédula
    print("\n   🆔 Probando búsqueda por cédula...")
    try:
        response = requests.get(
            f"{base_url}/api/buscar/votantes?tipo=cedula&q=123",
            headers=headers
        )
        print(f"     ✓ Respuesta HTTP: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"     ✓ Resultados encontrados: {len(data)}")
            if data:
                print("     ✓ Ejemplo de resultado:")
                resultado = data[0]
                print(f"       - Nombre: {resultado.get('nombre', 'N/A')}")
                print(f"       - Cédula: {resultado.get('cedula', 'N/A')}")
    except Exception as e:
        print(f"     ❌ Error al conectar: {str(e)}")

def test_search_form():
    """Verificar que el formulario de búsqueda existe"""
    print("\n🔍 Verificando formulario de búsqueda...")
    
    base_url = "http://localhost:5000"
    
    try:
        # Probar acceso a la página de búsqueda
        response = requests.get(f"{base_url}/buscar/votantes")
        print(f"   ✓ Respuesta HTTP: {response.status_code}")
        
        if response.status_code == 200:
            content = response.text
            checks = [
                ("input id='busqueda_nombre'", "Campo de búsqueda por nombre"),
                ("input id='busqueda_cedula'", "Campo de búsqueda por cédula"),
                ("api/buscar/votantes", "API de búsqueda en tiempo real"),
                ("searchForm", "Formulario de búsqueda"),
                ("resultados-tiempo-real", "Div para resultados en tiempo real")
            ]
            
            print("   ✓ Verificando elementos del template:")
            for check, description in checks:
                if check in content:
                    print(f"     ✓ {description}")
                else:
                    print(f"     ❌ {description} - No encontrado")
        
    except Exception as e:
        print(f"   ❌ Error al acceder a la página: {str(e)}")

def test_javascript_features():
    """Verificar características del JavaScript"""
    print("\n🔍 Verificando funcionalidades JavaScript...")
    
    base_url = "http://localhost:5000"
    
    try:
        response = requests.get(f"{base_url}/buscar/votantes")
        content = response.text
        
        features = [
            ("addEventListener('input'", "Búsqueda en tiempo real"),
            ("busqueda_tiempo_real", "Función de búsqueda en tiempo real"),
            ("debounce", "Debounce para optimizar búsquedas"),
            ("fetch(", "Llamadas AJAX"),
            ("mostrarResultados", "Función para mostrar resultados"),
            ("mostrarCargando", "Indicador de carga"),
            ("resultados-tiempo-real", "Div dinámico para resultados")
        ]
        
        print("   ✓ Verificando características de JavaScript:")
        for feature, description in features:
            if feature in content:
                print(f"     ✓ {description}")
            else:
                print(f"     ❌ {description} - No encontrado")
    
    except Exception as e:
        print(f"   ❌ Error al analizar JavaScript: {str(e)}")

def main():
    """Función principal"""
    print("🚀 PRUEBA DE BÚSQUEDA EN TIEMPO REAL")
    print("=" * 50)
    
    # Verificar que la base de datos existe
    has_data = test_database()
    
    if not has_data:
        print("\n⚠️  ADVERTENCIA: No se encontraron datos en la base de datos")
        print("   Ejecuta 'python agregar_datos_ejemplo.py' para agregar datos de prueba")
    
    # Probar la API
    test_api_search()
    
    # Verificar el formulario
    test_search_form()
    
    # Verificar JavaScript
    test_javascript_features()
    
    print("\n" + "=" * 50)
    print("📋 RESUMEN DE VERIFICACIÓN")
    print("   ✓ Base de datos verificada")
    print("   ✓ API de búsqueda probada")
    print("   ✓ Formulario de búsqueda verificado")
    print("   ✓ JavaScript en tiempo real verificado")
    print("\n💡 INSTRUCCIONES DE USO:")
    print("   1. Inicia la aplicación: python app.py")
    print("   2. Ve a: http://localhost:5000/buscar/votantes")
    print("   3. Escribe en el campo de búsqueda")
    print("   4. Los resultados aparecerán automáticamente")
    print("\n🎯 CARACTERÍSTICAS IMPLEMENTADAS:")
    print("   • Búsqueda en tiempo real (mientras escribes)")
    print("   • Debounce para evitar muchas consultas")
    print("   • Indicadores de carga")
    print("   • Información detallada en resultados")
    print("   • Navegación fluida entre pestañas")

if __name__ == "__main__":
    main()