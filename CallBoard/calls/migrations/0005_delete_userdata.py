# Generated by Django 5.0 on 2024-01-02 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0004_alter_userdata_birth_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserData',
        ),
    ]
