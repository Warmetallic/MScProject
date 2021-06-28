from django.urls import path, include
import django.contrib.auth.urls
from . import views
from django.http import Http404


urlpatterns = [
	path('', views.home, name="home"),
	path('accounts/', include('django.contrib.auth.urls')),
	path('signup/', views.signup, name='signup'),
    path('song/<int:id>/', views.song, name="song"),
    path('song_add/', views.song_add, name= 'song_add'),
    path('search', views.search, name= 'search'),
    # path('about/', views.about, name="about"),
	# path('details/<int:id>/', views.details, name="details"),
	# path('404', views.handler404, name="404"),
]
#handler404 = 'team.views.handler404'