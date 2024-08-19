# Generated by Django 5.0.7 on 2024-08-05 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=400)),
                ('author', models.CharField(max_length=80)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
