# Generated by Django 5.0 on 2023-12-29 14:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call_create_date', models.DateTimeField(auto_now_add=True)),
                ('call_header', models.CharField(max_length=128)),
                ('call_text', models.TextField()),
                ('call_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('call_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calls.category')),
            ],
        ),
        migrations.CreateModel(
            name='Respond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respond_text', models.TextField()),
                ('respond_create_date', models.DateTimeField(auto_now_add=True)),
                ('respond_accept', models.BooleanField(default=False)),
                ('respond_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('respond_call', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calls.call')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='calls.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('surname', models.CharField(max_length=32)),
                ('gender', models.CharField(choices=[('Ж', 'Женщина'), ('М', 'Мужчина')], default='М', max_length=7)),
                ('birth_date', models.DateField()),
                ('one_time_code', models.IntegerField(default=0)),
                ('one_time_code_update', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]