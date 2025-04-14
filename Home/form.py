from django import forms
from .models import *
import django_tables2 as tables


class ArticleWriteForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'Short_description', 'content', 'pub_date', 'icon_Name']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'Short_description', 'content', 'pub_date', 'icon_Name', 'status']
