from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .models import Song
from .forms import SignUpForm, SongForm



# Create your views here.
def home(request):
    songs = Song.objects.all()
    return render(request, 'home.html', {'songs': songs})


def song(request, id):
    song = get_object_or_404(Song, id=id)
    return render(request, 'song.html', {'song': song})
    

def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.customer.first_name = form.cleaned_data.get('first_name')
        user.customer.last_name = form.cleaned_data.get('last_name')
        user.customer.address = form.cleaned_data.get('address')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password= password)
        login(request, user)
        return redirect('/')
    return render(request, 'signup.html', {'form': form})


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        songs = Song.objects.filter(name__contains=searched)
        return render(request, 'search.html', {'searched': searched, 'songs': songs})
    else:
        return render(request, 'search.html', {})