from django import forms
from .models import Article

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Tu Nombre")
    email = forms.EmailField(label="Tu Email")
    message = forms.CharField(widget=forms.Textarea, label="Mensaje")

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ['title', 'content', 'category']
        labels = {
            'title': 'Título del Artículo',
            'content': 'Contenido',
            'category': 'Categoría',
        }