# Generated by Django 4.1.2 on 2022-10-29 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_rename_artiste_song_artiste_id_alter_lyric_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lyric',
            old_name='Song',
            new_name='song_id',
        ),
    ]
