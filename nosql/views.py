from django.shortcuts import render, redirect
from .connection import get_db
from .forms import ArticleNoSQLForm, CategoryNoSQLForm
from datetime import datetime


def list_article_view(request):

    db = get_db()

    coleccion = db.collection('articulos').stream()

    lista_final = []

    for documento in coleccion:
        datos = documento.to_dict()
        datos['id'] = documento.id
        lista_final.append(datos)
    
    return render(request, 'nosql/list.html', {'articles': lista_final})

def create_article_view(request):
    db = get_db()
    
    if request.method == 'POST':
        form = ArticleNoSQLForm(request.POST)
        # Capturamos la categoría del select manual
        cat_seleccionada = request.POST.get('category_select')
        
        if form.is_valid():
            data = form.cleaned_data
            
            nuevo_doc = {
                'title': data['title'],
                'content': data['content'],
                'category': cat_seleccionada, # Guardamos la del dropdown
                'date': datetime.now().strftime("%Y-%m-%d"),
                'author': 'Admin (Firebase)'
            }
            
            db.collection('articulos').add(nuevo_doc)
            return redirect('nosql_list')
    else:
        form = ArticleNoSQLForm()

    # Consultamos las categorías para llenar el <select>
    cats_ref = db.collection('categorias').stream()
    lista_categorias = []
    for doc in cats_ref:
        cat_data = doc.to_dict()
        cat_data['id'] = doc.id
        lista_categorias.append(cat_data)

    return render(request, 'nosql/form.html', {
        'form': form, 
        'categorias': lista_categorias
    })

def detail_view(request, doc_id):
    db = get_db()
    # Buscamos un documento específico por su ID
    doc = db.collection('articulos').document(doc_id).get()
    
    if doc.exists:
        article_data = doc.to_dict()
        article_data['id'] = doc.id
        return render(request, 'nosql/detail.html', {'article': article_data})
    else:
        return redirect('nosql_list')
    
def create_category_view(request):
    if request.method == 'POST':
        form = CategoryNoSQLForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            nueva_cat = {
                'name': data['name'],
                'description': data['description']
            }
            
            db = get_db()
            db.collection('categorias').add(nueva_cat)
            
            return redirect('nosql_list')
    else:
        form = CategoryNoSQLForm()
        
    return render(request, 'nosql/category_form.html', {'form': form})