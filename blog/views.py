from django.views.generic.base import TemplateView

class BlogView(TemplateView):
    template_name = 'index.html'
    extra_context = {
        'title':'Home'
    }