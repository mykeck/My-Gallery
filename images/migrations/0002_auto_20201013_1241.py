# Generated by Django 3.1.2 on 2020-10-13 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['location']},
        ),
    ]
