# Generated by Django 5.0 on 2024-01-02 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0002_remove_subscription_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='one_time_code',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='one_time_code_update',
        ),
        migrations.AlterField(
            model_name='call',
            name='call_category',
            field=models.CharField(choices=[('tanks', 'Танки'), ('hills', 'Хилы'), ('dd', 'ДД'), ('traders', 'Торговцы'), ('gild_masters', 'Гилдмастеры'), ('quest_givers', 'Квестгиверы'), ('blacksmiths', 'Кузнецы'), ('tanners', 'Кожевники'), ('potion_masters', 'Зельевары'), ('spell_masters', 'Мастера заклинаний')], default='tanks', max_length=14),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='gender',
            field=models.CharField(choices=[('W', 'Женщина'), ('M', 'Мужчина')], default='M', max_length=1),
        ),
    ]