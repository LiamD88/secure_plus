# Generated by Django 2.2.15 on 2020-10-10 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services1', '0004_auto_20201010_2052'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Packages',
            new_name='Package',
        ),
        migrations.AlterModelOptions(
            name='package',
            options={'verbose_name_plural': 'Packages'},
        ),
    ]
