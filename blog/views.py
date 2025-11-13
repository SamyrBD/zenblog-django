from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Article
from .forms import ContactForm

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