# Generated by Django 5.0.7 on 2024-08-12 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='computer',
        ),
    ]
