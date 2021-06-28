from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Song

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=50)
    address = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 
        'address', 'first_name', 'last_name', )

class SongForm (forms.ModelForm):
    songID = forms.CharField(max_length=30)
    # songName = forms.CharField(max_length=30)
    # songAuthor = forms.CharField(max_length=30)

    class Meta:
        model = Song
        fields = ('songID','songName','songAuthor','description','image')