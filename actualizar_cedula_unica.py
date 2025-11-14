#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para agregar restricción de cédula única a la base de datos
"""

import sqlite3

def actualizar_base_datos():
    """Actualiza la base de datos para hacer la cédula única"""
    
    print("🔧 Actualizando base de datos para cédula única...")
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    try:
        # Verificar si ya existe la restricción
        cursor.execute("PRAGMA table_info(votantes)")
        columns = cursor.fetchall()
        
        # Crear restricción única para número de cédula
        cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_cedula_unica ON votantes(numero_cedula)")
        
        print("✅ Restricción de cédula única agregada correctamente")
        
    except sqlite3.Error as e:
        print(f"❌ Error al actualizar base de datos: {e}")
    finally:
        conn.commit()
        conn.close()
    
    print("🎯 Base de datos actualizada para validación de cédula única")

if __name__ == "__main__":
    actualizar_base_datos()