from django.shortcuts import render
from django.views.generic.base import TemplateView
from article.views import ArticleEachCategory

class BlogView(TemplateView, ArticleEachCategory):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs) :
        articles = self.get_latest_article_each_category()
        context = {
            'latest_articles' : articles
        }
        return context

def page_not_found_view(request, exception):
    return render(request, "errors/404.html", status=404)

def error_view(request, exception=None):
    return render(request, "errors/500.html", status=500)

def permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", status=403)

def bad_request_view(request, exception=None):
    return render(request, "errors/400.html", status=400) 