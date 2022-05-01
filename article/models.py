from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy


# Create your models here.
class Article(models.Model):
    LIST_CATEGORY=(
        ('blog','Blog'),
        ('jurnal', 'Jurnal'),
        ('technology', 'Technology'),
        ('programming', 'Programming')
    )
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=50, default='blog', choices=LIST_CATEGORY)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.title)
        super().save()

    def get_absolute_url(self):
        return reverse_lazy('article:detail', kwargs={'slug': self.slug})
    
    def __str__(self) :
        return f"{self.id}. {self.title}"