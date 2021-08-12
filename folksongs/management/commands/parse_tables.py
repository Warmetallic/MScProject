"""
This file will populate the tables using Faker
"""

# Code for this page was adapted and inspired by the lectures from Dr Scharlau at the University of Aberdeen - in the 'Enterprise Software Development' module.

import random
import decimal
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from folksongs.models import Song

class Command(BaseCommand):
    help = 'Load data into the tables'

    def handle(self, *args, **options):

# drop the tables - use this order due to foreign keys - so that we can rerun the file as needed without repeating values
        Song.objects.all().delete()
        print("tables dropped successfully")

        fake = Faker()


        # create songs
        try:
            for i in range(10):
                song = Song.objects.create(
                name = fake.catch_phrase(),
                description = fake.catch_phrase(),
                )
                song.save()
        except:
            print("An error appeared during the song table creation")

        print("Product table was successfully created")