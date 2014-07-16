from django import forms
from django.forms import ModelForm
from registration.forms import RegistrationForm
from register.models import *

class ProfileForm(ModelForm):
    user = forms.CharField(widget=forms.HiddenInput())
    first_name = forms.CharField(required=False, max_length = 20, widget=forms.TextInput(attrs={'placeholder': 'first name', 'class':"form-control"}))
    last_name = forms.CharField(required=False, max_length = 20, widget=forms.TextInput(attrs={'placeholder': 'last name', 'class':"form-control"}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'about me..', 'class':"form-control"}))
    avatar = forms.ImageField(required=False)
    cover_image = forms.ImageField(required=False)
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio', 'user','avatar','cover_image']

class PostForm(ModelForm):
    content = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'What did you learn today? Share it to the world..', 'class':"form-control"}))
    source = forms.CharField(required=False, max_length=300,widget=forms.TextInput(attrs={'placeholder': 'Source', 'class':"form-control"}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': 'Description (optional)', 'class':"form-control"}))
    tag = forms.CharField(required=False, max_length=30,widget=forms.TextInput(attrs={'placeholder': 'Tags', 'class':"form-control"}))



    class Meta:
        model = Post
        fields = ["tag", "content", "source", "description"]