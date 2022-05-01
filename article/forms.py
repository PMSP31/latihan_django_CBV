from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'category'
        ]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class' : 'form-control col-sm-6',
                    'placeholder' : 'Article Title'
                }
            ),
            'content' : forms.Textarea(
                attrs={
                    'class' : 'form-control col-sm-6',
                    'placeholder' : 'Article Content'
                }
            ),
            'category' : forms.Select(
                attrs={
                    'class' : 'form-control col-sm-6'
                }
            )
        }