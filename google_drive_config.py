#!/usr/bin/env python3
"""
Configuración para sincronización real con Google Drive
Requiere configuración de Google Cloud Console
"""

import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
from datetime import datetime

# Scopes para Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def configurar_google_drive():
    """Configura la autenticación con Google Drive"""
    
    print("🔧 CONFIGURACIÓN DE GOOGLE DRIVE")
    print("=" * 40)
    
    print("\n📋 PASOS PARA CONFIGURAR:")
    print("1. Ve a Google Cloud Console (console.cloud.google.com)")
    print("2. Crea un nuevo proyecto o selecciona uno existente")
    print("3. Habilita la API de Google Drive")
    print("4. Crea credenciales (OAuth 2.0 Client ID)")
    print("5. Descarga el archivo 'credentials.json'")
    print("6. Coloca el archivo en esta carpeta")
    print("\n🚀 Después de configurar:")
    print("   python3 google_drive_real.py")
    
    # Verificar si existe credentials.json
    if os.path.exists('credentials.json'):
        print("\n✅ Archivo credentials.json encontrado")
        print("🔐 Iniciando autenticación...")
        return autenticar_google_drive()
    else:
        print("\n⚠️  Archivo credentials.json no encontrado")
        print("📥 Descárgalo desde Google Cloud Console")
        return False

def autenticar_google_drive():
    """Autentica con Google Drive API"""
    
    creds = None
    
    # El archivo token.pickle almacena los tokens de acceso y actualización del usuario
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # Si no hay credenciales (no está autenticado), inicia el flujo OAuth
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Guarda las credenciales para la próxima ejecución
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    # Construir servicio de Google Drive
    try:
        service = build('drive', 'v3', credentials=creds)
        print("✅ Conexión exitosa con Google Drive")
        return service
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False

def subir_archivo_drive(service, archivo_local, nombre_drive):
    """Sube un archivo a Google Drive"""
    try:
        # Definir metadatos del archivo
        file_metadata = {'name': nombre_drive}
        
        # Subir archivo
        media = MediaFileUpload(archivo_local)
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        
        print(f"✅ Subido: {nombre_drive} (ID: {file.get('id')})")
        return True
        
    except Exception as e:
        print(f"❌ Error subiendo {nombre_drive}: {e}")
        return False

def main():
    service = configurar_google_drive()
    
    if service:
        print("\n🌐 Conexión establecida con Google Drive")
        print("💡 Ahora puedes usar las funciones de sincronización")
        
        # Ejemplo: subir backup
        if os.path.exists('database.db'):
            subir_archivo_drive(service, 'database.db', f'database_{datetime.now().strftime("%Y%m%d_%H%M%S")}.db')

if __name__ == "__main__":
    main()