#!/usr/bin/env python3
"""
Script para crear una foto de prueba para testing de la funcionalidad de fotos ampliadas
"""

import sqlite3
import os
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def crear_foto_prueba():
    """Crea una imagen de prueba para un votante"""
    
    print("🎨 Creando foto de prueba...")
    
    # Crear directorio si no existe
    os.makedirs('uploads', exist_ok=True)
    
    # Nombre del archivo con timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"colaborador1_{timestamp}_foto_prueba.png"
    filepath = os.path.join('uploads', filename)
    
    # Crear imagen simple con PIL
    try:
        # Crear imagen
        img = Image.new('RGB', (300, 400), color=(70, 130, 180))  # Steel blue
        draw = ImageDraw.Draw(img)
        
        # Intentar usar fuente por defecto del sistema
        try:
            # Fuente más grande para texto
            font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
            font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
        except:
            font_large = ImageFont.load_default()
            font_medium = ImageFont.load_default()
        
        # Agregar texto simulado
        draw.text((50, 50), "FOTO DE PRUEBA", fill=(255, 255, 255), font=font_large)
        draw.text((50, 100), "Sistema de Votantes", fill=(255, 255, 255), font=font_medium)
        draw.text((50, 140), "Registrada automáticamente", fill=(200, 200, 200), font=font_medium)
        
        # Simular rostro con círculo
        draw.ellipse([100, 180, 200, 280], fill=(220, 220, 220), outline=(255, 255, 255), width=3)
        
        # Fecha
        draw.text((50, 320), f"Creada: {datetime.now().strftime('%Y-%m-%d %H:%M')}", 
                 fill=(200, 200, 200), font=font_medium)
        
        # Guardar imagen
        img.save(filepath, 'PNG')
        print(f"✅ Foto creada: {filepath}")
        
        # Actualizar base de datos
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # Asignar la foto al primer votante
        cursor.execute(
            "UPDATE votantes SET foto = ? WHERE id = 1",
            (filename,)
        )
        
        conn.commit()
        conn.close()
        
        print("✅ Foto asignada al votante ID 1")
        print("📋 Información:")
        print(f"   - Archivo: {filename}")
        print(f"   - Votante: ID 1 (primer votante en la base)")
        print(f"   - Ruta: /uploads/{filename}")
        print()
        print("🎯 Para probar:")
        print("   1. Inicia la aplicación: python app.py")
        print("   2. Login como colaborador")
        print("   3. Ve a 'Mis Votantes Registrados'")
        print("   4. Haz clic en la foto del primer votante")
        print("   5. ¡Se abrirá en modal ampliada!")
        
    except Exception as e:
        print(f"❌ Error creando foto: {e}")
        print("💡 La funcionalidad de fotos seguirá funcionando cuando subas fotos reales")

if __name__ == "__main__":
    crear_foto_prueba()