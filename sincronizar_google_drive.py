#!/usr/bin/env python3
"""
Script para sincronizar la base de datos con Google Drive
Crea respaldos automáticos y exporta datos para análisis
"""

import sqlite3
import shutil
import os
import json
from datetime import datetime
import pandas as pd

def crear_backup_database():
    """Crea un backup de la base de datos con timestamp"""
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_name = f'database_backup_{timestamp}.db'
    backup_path = os.path.join('backups', backup_name)
    
    # Crear carpeta backups si no existe
    os.makedirs('backups', exist_ok=True)
    
    # Copiar base de datos
    shutil.copy2('database.db', backup_path)
    print(f"✅ Backup creado: {backup_path}")
    
    return backup_path

def sincronizar_con_drive():
    """Simula sincronización con Google Drive (ajustar según tu configuración)"""
    
    # Rutas - AJUSTAR SEGÚN TU CONFIGURACIÓN
    drive_base_path = "/Users/[tu-usuario]/Google Drive/Campaña-Votantes"
    local_backup_path = "backups"
    
    print("🔄 Sincronizando con Google Drive...")
    print(f"📁 Destino: {drive_base_path}")
    
    # En un entorno real, aquí iría la lógica de Google Drive API
    # Por ahora, simulamos creando la estructura
    
    # Crear carpeta de exportación para análisis
    export_path = "exports"
    os.makedirs(export_path, exist_ok=True)
    
    return True

def exportar_datos_excel():
    """Exporta datos para análisis en Excel/CSV"""
    print("📊 Exportando datos para análisis...")
    
    conn = sqlite3.connect('database.db')
    
    # Consulta principal de votantes
    query_votantes = '''
    SELECT 
        v.id,
        v.nombre_completo,
        v.numero_cedula,
        v.telefono,
        v.direccion,
        v.escuela_votacion,
        v.fecha_registro,
        u.nombre as colaborador,
        v.latitud,
        v.longitud
    FROM votantes v
    JOIN usuarios u ON v.colaborador_id = u.id
    ORDER BY v.fecha_registro DESC
    '''
    
    # Cargar datos
    df_votantes = pd.read_sql_query(query_votantes, conn)
    
    # Exportar a Excel con múltiples hojas
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M')
    excel_file = f"exports/exportacion_completa_{timestamp}.xlsx"
    
    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
        # Hoja principal de votantes
        df_votantes.to_excel(writer, sheet_name='Votantes', index=False)
        
        # Hoja de resumen por colaborador
        df_resumen = df_votantes.groupby('colaborador').agg({
            'id': 'count',
            'fecha_registro': ['min', 'max']
        }).round(2)
        df_resumen.columns = ['Total_Votantes', 'Primera_Registro', 'Ultimo_Registro']
        df_resumen.to_excel(writer, sheet_name='Resumen_Colaboradores')
        
        # Hoja de estadísticas
        stats = {
            'Métrica': [
                'Total Votantes',
                'Votantes con Teléfono',
                'Votantes con Ubicación',
                'Colaboradores Activos',
                'Fecha Más Antigua',
                'Fecha Más Reciente'
            ],
            'Valor': [
                len(df_votantes),
                df_votantes['telefono'].notna().sum(),
                df_votantes[['latitud', 'longitud']].notna().all(axis=1).sum(),
                df_votantes['colaborador'].nunique(),
                df_votantes['fecha_registro'].min(),
                df_votantes['fecha_registro'].max()
            ]
        }
        df_stats = pd.DataFrame(stats)
        df_stats.to_excel(writer, sheet_name='Estadísticas', index=False)
    
    # Exportar también CSV simple
    csv_file = f"exports/votantes_simple_{timestamp}.csv"
    df_votantes.to_csv(csv_file, index=False, encoding='utf-8')
    
    conn.close()
    
    print(f"✅ Excel exportado: {excel_file}")
    print(f"✅ CSV exportado: {csv_file}")
    
    return excel_file, csv_file

def generar_reporte_json():
    """Genera un reporte en JSON para análisis programático"""
    conn = sqlite3.connect('database.db')
    
    # Estadísticas generales
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM votantes")
    total_votantes = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(DISTINCT colaborador_id) FROM votantes")
    total_colaboradores = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM votantes WHERE telefono IS NOT NULL")
    con_telefono = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM votantes WHERE latitud IS NOT NULL AND longitud IS NOT NULL")
    con_ubicacion = cursor.fetchone()[0]
    
    # Datos por colaborador
    cursor.execute('''
        SELECT u.nombre, COUNT(v.id) as total_votantes
        FROM usuarios u
        LEFT JOIN votantes v ON u.id = v.colaborador_id
        WHERE u.rol = 'colaborador'
        GROUP BY u.id, u.nombre
        ORDER BY total_votantes DESC
    ''')
    colaboradores_data = cursor.fetchall()
    
    conn.close()
    
    # Crear reporte
    reporte = {
        'fecha_generacion': datetime.now().isoformat(),
        'estadisticas_generales': {
            'total_votantes': total_votantes,
            'total_colaboradores': total_colaboradores,
            'votantes_con_telefono': con_telefono,
            'votantes_con_ubicacion': con_ubicacion,
            'porcentaje_con_telefono': round((con_telefono / total_votantes * 100), 2) if total_votantes > 0 else 0,
            'porcentaje_con_ubicacion': round((con_ubicacion / total_votantes * 100), 2) if total_votantes > 0 else 0
        },
        'desglose_por_colaborador': [
            {
                'colaborador': nombre,
                'votantes_registrados': total
            }
            for nombre, total in colaboradores_data
        ]
    }
    
    # Guardar JSON
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M')
    json_file = f"exports/reporte_campana_{timestamp}.json"
    
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(reporte, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Reporte JSON generado: {json_file}")
    return json_file

def main():
    """Función principal de sincronización"""
    print("🔄 SINCRONIZACIÓN CON GOOGLE DRIVE")
    print("=" * 50)
    
    # Verificar que existe la base de datos
    if not os.path.exists('database.db'):
        print("❌ Error: No se encontró database.db")
        return False
    
    try:
        # 1. Crear backup
        print("\n1️⃣ Creando backup de la base de datos...")
        backup_path = crear_backup_database()
        
        # 2. Sincronizar (simulado)
        print("\n2️⃣ Preparando sincronización...")
        sincronizar_con_drive()
        
        # 3. Exportar datos
        print("\n3️⃣ Exportando datos para análisis...")
        excel_file, csv_file = exportar_datos_excel()
        
        # 4. Generar reporte
        print("\n4️⃣ Generando reporte de estadísticas...")
        json_file = generar_reporte_json()
        
        print("\n" + "=" * 50)
        print("✅ SINCRONIZACIÓN COMPLETADA")
        print(f"📁 Archivos generados:")
        print(f"   • Backup: {backup_path}")
        print(f"   • Excel: {excel_file}")
        print(f"   • CSV: {csv_file}")
        print(f"   • JSON: {json_file}")
        print(f"\n💡 Para subir manualmente a Google Drive:")
        print(f"   1. Ve a drive.google.com")
        print(f"   2. Arrastra las carpetas 'backups' y 'exports'")
        print(f"   3. ¡Listo! Tus datos estarán seguros en la nube")
        
        return True
        
    except Exception as e:
        print(f"❌ Error durante la sincronización: {str(e)}")
        return False

if __name__ == "__main__":
    main()