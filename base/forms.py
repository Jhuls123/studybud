from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from .models import Post


class AddPostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['author']

class CreateUserForm(UserCreationForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={
    #     "class":"username-input",
    #     "type":"text",
    #     "placeholder":"enter your username..."
    # }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class":"username-input",
        "type":"text",
        "placeholder":"enter your first name..."
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class":"username-input",
        "type":"text",
        "placeholder":"enter your last name..."
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        "class":"username-input",
        "type":"email",
        "placeholder":"enter your email..."
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class":"username-input",
        "type":"password",
        "placeholder":"enter your password..."
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class":"username-input",
        "type":"password",
        "placeholder":"confirm password..."
    }))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={"class":"username-input","placeholder":"enter your username...."}),
        }