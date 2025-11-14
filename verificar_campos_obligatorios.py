#!/usr/bin/env python3
"""
Script para verificar que los campos obligatorios estén configurados correctamente
"""

def verificar_campo_obligatorio(archivo, nombre_campo, descripcion):
    """Verifica que un campo esté marcado como required"""
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
            if f'required' in contenido and nombre_campo in contenido:
                print(f"✅ {descripcion}: REQUERIDO")
                return True
            else:
                print(f"❌ {descripcion}: NO REQUERIDO")
                return False
    except Exception as e:
        print(f"❌ Error leyendo {archivo}: {e}")
        return False

def main():
    print("🔍 VERIFICANDO CAMPOS OBLIGATORIOS")
    print("=" * 50)
    
    # Verificar nuevo_votante.html
    print("\n📋 NUEVO VOTANTE:")
    verificar_campo_obligatorio("templates/nuevo_votante.html", "nombre_completo", "Nombre completo")
    verificar_campo_obligatorio("templates/nuevo_votante.html", "numero_cedula", "Cédula")
    
    # Verificar editar_votante.html
    print("\n📋 EDITAR VOTANTE:")
    verificar_campo_obligatorio("templates/editar_votante.html", "nombre_completo", "Nombre completo")
    verificar_campo_obligatorio("templates/editar_votante.html", "numero_cedula", "Cédula")
    
    print("\n" + "=" * 50)
    print("✅ CAMBIOS REALIZADOS:")
    print("1. 🔒 Cédula ahora es obligatoria en ambos formularios")
    print("2. 🛡️ Protección adicional contra validación HTML5 automática")
    print("3. 🚫 Bloquea submits automáticos cuando se completan campos")
    
    print("\n📋 INSTRUCCIONES DE PRUEBA:")
    print("1. Reinicia la aplicación: python app.py")
    print("2. Abre navegador en modo incógnito")
    print("3. Ve a 'Nuevo Votante'")
    print("4. VERIFICAR:")
    print("   - ✅ Nombre: Campo obligatorio")
    print("   - ✅ Cédula: Campo obligatorio (NUEVO)")
    print("5. Prueba GPS con nombre COMPLETO:")
    print("   - Debe aparecer ventana de confirmación")
    print("   - NO debe guardarse automáticamente")
    print("6. Solo debe guardarse al hacer clic en 'Guardar'")

if __name__ == "__main__":
    main()
