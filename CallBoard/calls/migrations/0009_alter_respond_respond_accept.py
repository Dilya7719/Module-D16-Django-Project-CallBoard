# Generated by Django 5.0 on 2024-01-03 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0008_remove_call_call_img_min'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respond',
            name='respond_accept',
            field=models.BooleanField(),
        ),
    ]