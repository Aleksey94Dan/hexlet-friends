# Generated by Django 2.2.5 on 2019-09-28 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=200, verbose_name='Логин')),
                ('commits', models.IntegerField(default=0, verbose_name='Количество коммитов')),
                ('pull_requests', models.IntegerField(default=0, verbose_name='Количество pr')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
