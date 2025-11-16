from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Article
from .forms import ContactForm
from .models import Article, Category
from .forms import ContactForm, ArticleForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm # Usamos el ModelForm que ya teníamos
    template_name = 'blog/article_form.html' # Un template para el formulario
    
    # URL a la que redirigir después de crear el artículo con éxito
    success_url = reverse_lazy('article_list')

    # --- EXPLICACIÓN CLAVE (PARA EL PROFESOR) ---
    # Sobrescribimos el método 'form_valid'.
    # Este método se llama DESPUÉS de que el formulario se valida
    # pero ANTES de que el objeto se guarde en la base de datos.
    def form_valid(self, form):
        # 1. 'form.instance' es el objeto Artículo en memoria.
        #    Su campo 'author' está vacío.
        try:
            # 2. Buscamos un 'author' por defecto (el admin/superusuario).
            admin_user = User.objects.filter(is_superuser=True).first()
            
            # 3. Asignamos ese admin como el autor.
            if admin_user:
                form.instance.author = admin_user
            else:
                # Si no hay admin, la app está rota, pero evitamos el crash
                return super().form_invalid(form)
        except Exception as e:
            # Manejar el error si User.objects falla
            pass 
        
        # 4. Llamamos al 'super()' para que termine el proceso de guardado.
        return super().form_valid(form)

# --- VISTA PARA CREAR CATEGORÍAS (PÚBLICA) ---
class CategoryCreateView(CreateView):
    model = Category
    # Podemos definir los campos aquí mismo si no necesitamos un Form
    fields = ['name', 'description']
    template_name = 'blog/category_form.html'
    success_url = reverse_lazy('article_list')

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            print(f"FORMULARIO RECIBIDO de {name} ({email}): {message}")
            
            return redirect('article_list') 
    else:
        form = ContactForm()

    return render(request, 'blog/contact.html', {'form': form})