from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj) :
        user = request.user
        if obj != None :
            if user.has_perm('article.publish_article'):
                readonly_fields = [
                        'author',
                        'slug', 
                        'published', 
                        'updated'
                    ]
                return readonly_fields
            elif user.has_perm('article.add_article'):
                if obj.is_published:
                    return [field.name for field in Article._meta.fields]
                else:
                    readonly_fields = [
                            'author',
                            'slug',
                            'is_published',
                            'published', 
                            'updated'
                        ]
                    return readonly_fields
        else:
            readonly_fields = [
                    'author',
                    'slug',
                    'is_published',
                    'published', 
                    'updated'
                ]
            return readonly_fields
            
admin.site.register(Article, ArticleAdmin)