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