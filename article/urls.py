from django.urls import path
from .views import ArticleCategoryListView, ArticleDetailView, ArticleListView

app_name = 'article'
urlpatterns = [
    path('<int:page>', ArticleListView.as_view(), name='list'),
    path('detail/<slug:slug>', ArticleDetailView.as_view(), name='detail'),
    path('category/<str:category>', ArticleCategoryListView.as_view(), name='category')
]