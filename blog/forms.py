# blog/forms.py

from django import forms
from .models import Article  # <-- Importa el modelo Article

# --- 1. El formulario de contacto (este ya lo tenías) ---
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Tu Nombre")
    email = forms.EmailField(label="Tu Email")
    message = forms.CharField(widget=forms.Textarea, label="Mensaje")


# --- 2. El formulario que faltaba (basado en el Modelo) ---
class ArticleForm(forms.ModelForm):
    # ModelForm crea un formulario directamente desde tu modelo 'Article'
    
    class Meta:
        model = Article
        
        # 'fields' le dice qué campos del modelo mostrar en el formulario.
        # Omitimos 'author' (porque lo asignamos en la vista) y
        # 'publication_date' (porque es 'auto_now_add=True').
        fields = ['title', 'content', 'category']
        
        # (Opcional) Puedes añadir etiquetas si quieres
        labels = {
            'title': 'Título del Artículo',
            'content': 'Contenido',
            'category': 'Categoría',
        }