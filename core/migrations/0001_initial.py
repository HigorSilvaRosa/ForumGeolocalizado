# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
                ('creation_date', models.DateTimeField(auto_now=True, verbose_name='Data de cria\xe7\xe3o')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='Data de modifica\xe7\xe3o')),
                ('content', models.TextField(verbose_name='Texto')),
            ],
            options={
                'verbose_name': 'Postagem',
                'verbose_name_plural': 'Postagens',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
                ('creation_date', models.DateTimeField(auto_now=True, verbose_name='Data de cria\xe7\xe3o')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='Data de modifica\xe7\xe3o')),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
                ('user', models.ForeignKey(verbose_name='Criador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'T\xf3pico',
                'verbose_name_plural': 'T\xf3picos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(verbose_name='T\xf3pico', to='core.Topic'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(verbose_name='Criador', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
