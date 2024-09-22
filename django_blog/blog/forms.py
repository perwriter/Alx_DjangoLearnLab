from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from taggit.forms import TagWidget


class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Username...", "autofocus": "autofocus"}
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "you@email.com"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "password1": forms.PasswordInput(),
                "placeholder": "Enter Password...",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "password2": forms.PasswordInput(),
                "placeholder": "Re-enter Password...",
            }
        )
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 5:
            raise forms.ValidationError('Comment must be at least 5 characters long.')
        return content