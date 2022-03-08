# Generated by Django 3.2.12 on 2022-03-08 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=20, unique=True)),
                ('age', models.SmallIntegerField(default=0)),
                ('phone', models.SmallIntegerField(blank=True, db_index=True, default=0)),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('info', models.TextField()),
                ('crete_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
