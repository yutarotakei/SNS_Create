from django import forms
from.models import Message
from django.contrib.auth.models import User

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100)

class PostForm(forms.Form):
    content = forms.Charfield(max_length=500, widget=forms.Textarea)

