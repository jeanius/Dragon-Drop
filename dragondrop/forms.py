from django import forms
from dragondrop.models import Folder, Bookmark, BinFolder
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(max_length=60, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


        
class PageForm(forms.ModelForm):
    url = forms.URLField(max_length=200, help_text="Paste the URL of a page")

    class Meta:
        model = Bookmark
        fields = ('url')
