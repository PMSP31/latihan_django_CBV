from django.views.generic import ListView, DetailView
from .models import Article

# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'article/article_list.html'
    context_object_name = 'articles'
    ordering = ['-published']
    paginate_by = 3
    extra_context = {}
    
    # get all category
    def get_context_data(self, **kwargs):
        categories = self.model.objects.values_list('category', flat = True).distinct()
        self.extra_context['categories'] = categories
        context = super().get_context_data(**kwargs)
        return context
    
class ArticleCategoryListView(ListView):
    model = Article
    template_name = 'article/article_category_list.html'
    context_object_name = 'articles'
    ordering = ['-published']
    paginate_by = 3
    extra_context = {}

    # query by category from kwargs
    def get_queryset(self):
        self.queryset = self.model.objects.filter(category = self.kwargs['category'])
        self.extra_context['title'] =  f"Article {self.kwargs['category']}"
        queryset = super().get_queryset()
        return queryset
    
    def get_context_data(self, **kwargs):
        categories = self.model.objects.values_list('category', flat = True).distinct().exclude(category = self.kwargs['category'])
        self.extra_context['categories'] = categories
        context = super().get_context_data(**kwargs)
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/article_detail.html'
    context_object_name = 'article'
    extra_context = {}

    def get_context_data(self, **kwargs):
        categories = self.model.objects.values_list('category', flat = True).distinct().exclude(category = self.object.category)
        self.extra_context['categories'] = categories

        related_articles = self.model.objects.filter(category = self.object.category).exclude(id = self.object.id)
        self.extra_context['related_articles'] = related_articles

        context = super().get_context_data(**kwargs)
        return context