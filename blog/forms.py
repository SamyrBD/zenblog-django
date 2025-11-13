from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Tu Nombre")
    email = forms.EmailField(label="Tu Email")
    message = forms.CharField(widget=forms.Textarea, label="Mensaje")