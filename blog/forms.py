from django import forms
from .models import Post
from django.db import models
from tinymce.widgets import TinyMCE

class AddPostForm(forms.ModelForm):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
    class Meta:
        model = Post
        fields = ['title', 'created_date', 'published_date', 'content']
        formfield_overrides = {
            models.TextField: {'widget': TinyMCE()},
        }