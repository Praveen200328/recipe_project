# Generated by Django 5.0.6 on 2024-06-14 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='is_email_verifies',
            new_name='is_email_verified',
        ),
    ]
