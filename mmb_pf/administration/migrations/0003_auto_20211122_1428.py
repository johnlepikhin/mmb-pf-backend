# Generated by Django 3.2.9 on 2021-11-22 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_remove_mainmenu_personnel_access'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mmbpfusers',
            name='fact_address',
        ),
        migrations.AddField(
            model_name='mmbpfusers',
            name='tourist_club',
            field=models.CharField(blank=True, default='', help_text='Название туристического клуба если есть', max_length=1024),
        ),
        migrations.AddField(
            model_name='mmbpfusers',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Организатор'), (2, 'Участник')], default=2, help_text='Тип пользователя'),
        ),
    ]
