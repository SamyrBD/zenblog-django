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
    form_class = ArticleForm
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('article_list')

    def form_valid(self, form):
        try:
            admin = User.objects.filter(is_superuser=True).first()
            form.instance.author = admin 
        except:
            pass
        return super().form_valid(form)

class CategoryCreateView(CreateView):
    model = Category
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