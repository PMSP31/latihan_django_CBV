from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'category',
            'is_published'
        ]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Article Title'
                }
            ),
            'content' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Article Content'
                }
            ),
            'category' : forms.Select(
                attrs={
                    'class' : 'form-control'
                }
            ),
            'is_published' : forms.CheckboxInput(
                attrs={
                    'class' : 'form-check-input'
                }
            )
        }