from django.contrib import admin
from django.urls import path, include
from .views import BlogView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BlogView.as_view(), name='index'),
    path('account/',include('django.contrib.auth.urls')),
    path('account/', include('account.urls', namespace = 'account')),
    path('article/', include('article.urls', namespace = 'article'))
]
