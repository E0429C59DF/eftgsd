from django import forms
from django.db import models
from forum_app.models import beitrag

class User_Login(forms.Form):
    email = forms.EmailField(label=False ,widget= forms.TextInput(attrs={'placeholder': 'E-Mail'}))
    passwort = forms.CharField(label=False ,widget=forms.PasswordInput(attrs={'placeholder': 'Passwort'}))

class PostBeitrag(forms.ModelForm):
    class Meta:
        model = beitrag
        fields = ['titel', 'beitrag']
        widgets = {'beitrag': forms.Textarea(attrs={'placeholder': 'Beitrag'}), 
                   'titel':forms.TextInput(attrs={'placeholder': 'Titel'})}