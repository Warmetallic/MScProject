# Code for this page was adapted and inspired by the lectures from Dr Scharlau at the University of Aberdeen - in the 'Enterprise Software Development' module.


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('folksongs.urls')),

]