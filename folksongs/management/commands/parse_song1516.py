import random
import decimal
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from folksongs.models import Song


class Command(BaseCommand):
    help = 'Load data into the tables'



    def handle(self, *args, **options):
        with open('static/imgGleb/test.txt', 'r') as file:
            data = file.read().replace('\n', '')
            
            song = Song.objects.create(
                songID = '1516',
                songName = 'The Emigrant’s Farewell to Donside,\n The Donside Emigrant’s'+ 
                'Farewell,\n Come All My Dear Comrades,\n The Farewell',
                songAuthor = 'JAMES ANGUS,\n NORMAN FARQUHARSON,\n'+ 
                'JONATHAN GAULD and Mrs BEGG,\n Mrs MARGARET GILLESPIE and Rev. JAMES B. DUNCAN-D &G,\n'+
                'GEORGE F. DUNCAN,\n ROBERT ALEXANDER,\n ALEX MURISON,\n GEORGE CORBET,\n J. W. SPENCE,'+
                '\n G. G. FARQUHAR,\n GEORGE ANDERSON or J. CALDER,\n Mrs STUART',
                description = 'some data'
                )
            song.save()