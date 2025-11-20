import firebase_admin
from firebase_admin import credentials, firestore
import os
from django.conf import settings

def get_db():
    # Verificamos si ya estamos conectados para no dar error
    if not firebase_admin._apps:
        # Ruta dinámica al archivo JSON que pusiste junto a manage.py
        cred_path = os.path.join(settings.BASE_DIR, 'firebase_credentials.json')
        
        # Cargamos la credencial
        cred = credentials.Certificate(cred_path)
        
        # Iniciamos la app
        firebase_admin.initialize_app(cred)
    
    # Devolvemos el cliente de base de datos
    return firestore.client()