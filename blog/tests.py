from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Category, Article

class BlogTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(name='Bienestar')
        self.article = Article.objects.create(
            title='Prueba de Artículo',
            content='Este es el contenido de prueba.',
            author=self.user,
            category=self.category
        )

    def test_model_article_str(self):
        self.assertEqual(str(self.article), 'Prueba de Artículo')

    def test_model_category_str(self):
        self.assertEqual(str(self.category), 'Bienestar')

    def test_article_list_view(self):
        url = reverse('article_list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Prueba de Artículo')
        self.assertTemplateUsed(response, 'blog/article_list.html')

    def test_article_detail_view(self):
        url = reverse('article_detail', args=[self.article.pk])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Este es el contenido de prueba.')
        self.assertTemplateUsed(response, 'blog/article_detail.html')

    def test_article_detail_404(self):
        url = reverse('article_detail', args=[999]) # ID que no existe
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
