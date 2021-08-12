#This is a test to insert a song into the database

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
                name = 'This is the title',
                description = data,
                )
            song.save()

