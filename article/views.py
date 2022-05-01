from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ArticleForm
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
        self.extra_context['active_category'] =  self.kwargs['category']
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

class ArticleCreateView(CreateView):
    form_class = ArticleForm
    template_name = 'article/article_create.html'

class ArticleManageView(ListView):
    model = Article
    template_name = 'article/article_manage.html'
    context_object_name = 'articles'
    ordering = ['-published']

class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article/article_update.html'

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('article:manage')

class ArticleEachCategory():
    model = Article

    def get_latest_article_each_category(self):
        categories = self.model.objects.values_list('category', flat=True).distinct()
        querysets = []

        for category in categories :
            article = self.model.objects.filter(category = category).latest('published')
            querysets.append(article)

        return querysets