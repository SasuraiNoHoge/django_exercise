from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')

class PhotoForm(forms.Form):
    image = forms.ImageField()