from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView,LogoutView
from .views import BlogView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BlogView.as_view(), name='index'),
    path('login/',LoginView.as_view(redirect_authenticated_user = True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('account/', include('account.urls', namespace = 'account')),
    path('article/', include('article.urls', namespace = 'article'))
]

handler404 = 'blog.views.page_not_found_view'
handler500 = 'blog.views.error_view'
handler403 = 'blog.views.permission_denied_view'
handler400 = 'blog.views.bad_request_view'
