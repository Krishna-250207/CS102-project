# Generated by Django 2.1.7 on 2019-03-26 11:54

import accounts.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', accounts.managers.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
