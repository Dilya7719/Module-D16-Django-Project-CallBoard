# Generated by Django 5.0 on 2024-01-04 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0009_alter_respond_respond_accept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respond',
            name='respond_accept',
            field=models.BooleanField(null=True),
        ),
    ]