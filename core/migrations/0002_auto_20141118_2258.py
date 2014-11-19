# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
                ('creation_date', models.DateTimeField(auto_now=True, verbose_name='Data de cria\xe7\xe3o')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='Data de modifica\xe7\xe3o')),
                ('post', models.ForeignKey(related_name='reports', verbose_name='Post', to='core.Post')),
                ('user', models.ForeignKey(related_name='post_reports', verbose_name='Usu\xe1rio', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Postagem reportada',
                'verbose_name_plural': 'Postagens reportadas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TopicReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
                ('creation_date', models.DateTimeField(auto_now=True, verbose_name='Data de cria\xe7\xe3o')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='Data de modifica\xe7\xe3o')),
                ('post', models.ForeignKey(related_name='reports', verbose_name='Post', to='core.Topic')),
                ('user', models.ForeignKey(related_name='topic_reports', verbose_name='Usu\xe1rio', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'T\xf3pico reportado',
                'verbose_name_plural': 'T\xf3picos reportados',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(related_name='posts', verbose_name='T\xf3pico', to='core.Topic'),
            preserve_default=True,
        ),
    ]
