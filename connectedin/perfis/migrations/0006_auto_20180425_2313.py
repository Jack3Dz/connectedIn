# Generated by Django 2.0.3 on 2018-04-26 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0005_auto_20180424_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='usuarios',
            new_name='usuario',
        ),
    ]
