# Generated by Django 4.1.3 on 2023-02-03 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geultarae', '0004_user_chosen writings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Chosen writings',
        ),
        migrations.AddField(
            model_name='user',
            name='writings',
            field=models.CharField(default='', max_length=200, verbose_name='String of ids'),
            preserve_default=False,
        ),
    ]
