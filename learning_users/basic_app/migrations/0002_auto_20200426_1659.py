# Generated by Django 3.0.5 on 2020-04-26 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='profile_pci',
            new_name='profile_pic',
        ),
    ]
