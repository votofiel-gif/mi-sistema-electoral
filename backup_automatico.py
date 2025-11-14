#!/usr/bin/env python3
"""
Script de backup automático que se puede ejecutar con cron
"""

import sqlite3
import shutil
import os
from datetime import datetime

def backup_database():
    """Crea un backup de la base de datos"""
    if not os.path.exists('database.db'):
        print("❌ Base de datos no encontrada")
        return False
    
    # Crear carpeta de backups
    os.makedirs('backups', exist_ok=True)
    
    # Nombre del backup con timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = f'backups/database_{timestamp}.db'
    
    # Copiar archivo
    shutil.copy2('database.db', backup_file)
    
    # Mantener solo los últimos 30 backups
    mantener_ultimos_backups('backups', 30)
    
    print(f"✅ Backup creado: {backup_file}")
    return True

def mantener_ultimos_backups(carpeta, cantidad_maxima):
    """Mantiene solo los N backups más recientes"""
    if not os.path.exists(carpeta):
        return
    
    # Obtener todos los archivos de backup
    archivos = []
    for archivo in os.listdir(carpeta):
        if archivo.startswith('database_') and archivo.endswith('.db'):
            ruta_completa = os.path.join(carpeta, archivo)
            timestamp = os.path.getmtime(ruta_completa)
            archivos.append((timestamp, ruta_completa))
    
    # Ordenar por fecha (más reciente primero)
    archivos.sort(reverse=True)
    
    # Eliminar los más antiguos si hay demasiados
    for timestamp, ruta in archivos[cantidad_maxima:]:
        try:
            os.remove(ruta)
            print(f"🗑️  Backup antiguo eliminado: {os.path.basename(ruta)}")
        except Exception as e:
            print(f"⚠️  No se pudo eliminar {ruta}: {e}")

def main():
    print(f"💾 Backup Automático - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    backup_database()

if __name__ == "__main__":
    main()