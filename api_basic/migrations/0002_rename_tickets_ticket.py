# Generated by Django 3.2.4 on 2021-07-13 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tickets',
            new_name='Ticket',
        ),
    ]