# Generated by Django 4.0.1 on 2022-03-27 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0003_alter_game_cover_alter_game_first_release_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='first_release_date',
            field=models.DateTimeField(),
        ),
    ]
