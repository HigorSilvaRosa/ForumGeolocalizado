# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20141204_2118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usercoordinates',
            options={'verbose_name': 'Coordenadas de usu\xe1rio', 'verbose_name_plural': 'Coordenadas de usu\xe1rio'},
        ),
        migrations.AddField(
            model_name='topic',
            name='latitude',
            field=models.FloatField(default=0, verbose_name='Latitude'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='topic',
            name='longitude',
            field=models.FloatField(default=0, verbose_name='Longitude'),
            preserve_default=True,
        ),
    ]
