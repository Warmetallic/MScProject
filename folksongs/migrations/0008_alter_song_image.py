# Generated by Django 3.2.3 on 2021-06-28 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folksongs', '0007_alter_song_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
