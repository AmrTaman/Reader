# Generated by Django 5.1.1 on 2024-09-11 06:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True,
                 null=True, upload_to='books/images/')),
                ('copies_left', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.category')),
            ],
        ),
    ]
