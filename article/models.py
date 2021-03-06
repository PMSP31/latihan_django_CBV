from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.models import User
from .validators import validate_title
from profanity.validators import validate_is_profane

# Create your models here.
class Article(models.Model):
    LIST_CATEGORY=(
        ('blog','Blog'),
        ('jurnal', 'Jurnal'),
        ('technology', 'Technology'),
        ('programming', 'Programming')
    )
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100, validators=[validate_title, validate_is_profane])
    content = models.TextField(validators=[validate_is_profane])
    category = models.CharField(max_length=50, default='blog', choices=LIST_CATEGORY)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    published = models.DateTimeField(null=True)
    slug = models.SlugField(blank=True, editable=False)

    class Meta:
        # custom permissions
        permissions = (
            ('publish_article', 'Can publish article'),
        )

    def save(self):
        self.slug = slugify(self.title)
        if self.is_published == True:
            self.published = timezone.now()
        else:
            self.published = None
            
        super().save()

    def get_absolute_url(self):
        return reverse_lazy('article:detail', kwargs={'slug': self.slug})
    
    def __str__(self) :
        return f"{self.id}. {self.title}"