# Generated by Django 3.2.3 on 2021-06-08 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('address', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]
