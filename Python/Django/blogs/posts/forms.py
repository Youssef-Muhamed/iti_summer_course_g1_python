from django import forms
from django.forms import ModelForm

from category.models import Category
from posts.models import Post

# class PostForm(forms.Form):
#     title = forms.CharField(max_length=200,label='Title')
#     description = forms.CharField(widget=forms.Textarea)
#     image = forms.ImageField()
#     version = forms.IntegerField()
#     author = forms.CharField()
#     category = forms.ModelChoiceField(queryset=Category.objects.all())

class PostModelForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'