# Generated by Django 4.1.1 on 2022-09-30 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheetdata',
            name='number',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Номер'),
            preserve_default=False,
        ),
    ]
