from django import forms

from blogs.models import Blog
from recipes_user.models import RecipeUser

class BlogForm(forms.Form):
    blog_title = forms.CharField(max_length=30)
    blog_body = forms.CharField(widget=forms.Textarea)
    blog_author = forms.ModelChoiceField(queryset=RecipeUser.objects.all())