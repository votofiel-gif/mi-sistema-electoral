#!/usr/bin/env python3
"""
Script para actualizar la base de datos agregando el campo numero_cedula
"""

import sqlite3
import os

def actualizar_base_datos():
    """Actualiza la base de datos agregando la columna numero_cedula"""
    
    # Conectar a la base de datos
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    try:
        # Verificar si la columna ya existe
        cursor.execute("PRAGMA table_info(votantes)")
        columnas = [column[1] for column in cursor.fetchall()]
        
        if 'numero_cedula' not in columnas:
            print("🔄 Agregando columna numero_cedula a la tabla votantes...")
            cursor.execute("ALTER TABLE votantes ADD COLUMN numero_cedula TEXT")
            print("✅ Columna numero_cedula agregada exitosamente")
        else:
            print("ℹ️ La columna numero_cedula ya existe en la tabla votantes")
        
        # Agregar algunos datos de ejemplo de cédulas para los votantes existentes
        print("🔄 Actualizando datos de ejemplo con números de cédula...")
        
        # Obtener todos los votantes actuales
        cursor.execute("SELECT id FROM votantes")
        votantes = cursor.fetchall()
        
        # Agregar cédulas de ejemplo (números ficticios para Paraguay)
        cedulas_ejemplo = [
            "1234567", "2345678", "3456789", "4567890", "5678901", 
            "6789012", "7890123", "8901234", "9012345", "0123456",
            "1123456", "2234567"
        ]
        
        for i, (votante_id,) in enumerate(votantes):
            if i < len(cedulas_ejemplo):
                cursor.execute(
                    "UPDATE votantes SET numero_cedula = ? WHERE id = ?",
                    (cedulas_ejemplo[i], votante_id)
                )
        
        conn.commit()
        print(f"✅ {min(len(votantes), len(cedulas_ejemplo))} cédulas de ejemplo agregadas")
        
        # Verificar el resultado
        cursor.execute("SELECT COUNT(*) as total, COUNT(numero_cedula) as con_cedula FROM votantes")
        resultado = cursor.fetchone()
        total, con_cedula = resultado
        
        print(f"📊 Base de datos actualizada:")
        print(f"   - Total de votantes: {total}")
        print(f"   - Con número de cédula: {con_cedula}")
        
    except Exception as e:
        print(f"❌ Error al actualizar la base de datos: {e}")
        conn.rollback()
    finally:
        conn.close()
        print("✅ Base de datos cerrada")

if __name__ == "__main__":
    actualizar_base_datos()