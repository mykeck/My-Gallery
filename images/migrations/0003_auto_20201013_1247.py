# Generated by Django 3.1.2 on 2020-10-13 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20201013_1241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='category',
            new_name='categories',
        ),
    ]