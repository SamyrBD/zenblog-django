from django import forms

# NOTA PROFE: Como NoSQL no tiene modelos estrictos, usamos un formulario simple
# para validar que nos envíen texto y no cosas vacías.
class ArticleNoSQLForm(forms.Form):
    title = forms.CharField(label="Título del Artículo", max_length=100)
    content = forms.CharField(label="Contenido", widget=forms.Textarea)
    category = forms.CharField(label="Categoría", required=False)

class CategoryNoSQLForm(forms.Form):
    name = forms.CharField(label="Nombre de la Categoría", max_length=100)
    description = forms.CharField(label="Descripción", widget=forms.Textarea, required=False)