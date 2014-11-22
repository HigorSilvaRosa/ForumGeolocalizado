# coding=utf-8
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.base import Model
from django.db.models.fields import CharField, TextField, DateTimeField, BooleanField
from django.db.models.fields.related import ForeignKey


class BaseModel(Model):
    is_active = BooleanField(default=True)
    creation_date = DateTimeField(auto_now=True, verbose_name=u"Data de criação")
    modification_date = DateTimeField(auto_now=True, verbose_name=u"Data de modificação")
    class Meta:
        abstract = True

class Topic(BaseModel):
    name = CharField(max_length=150, verbose_name=u"Nome")
    user = ForeignKey(User, verbose_name=u"Criador")
    
    class Meta:
        verbose_name = u"Tópico"
        verbose_name_plural = u"Tópicos"
    
class Post(BaseModel):
    topic = ForeignKey(Topic, related_name="posts", verbose_name=u"Tópico")
    user = ForeignKey(User, verbose_name=u"Criador")
    content = TextField(verbose_name=u"Texto")

    class Meta:
        verbose_name = u"Postagem"
        verbose_name_plural = u"Postagens"
        ordering = ["-id"]


class TopicReport(BaseModel):
    post=ForeignKey(Topic, related_name="reports", verbose_name=u"Post")
    user=ForeignKey(User, related_name="topic_reports", verbose_name=u"Usuário")

    class Meta:
        verbose_name = u"Tópico reportado"
        verbose_name_plural = u"Tópicos reportados"

class PostReport(BaseModel):
    post=ForeignKey(Post, related_name="reports", verbose_name=u"Post")
    user=ForeignKey(User, related_name="post_reports", verbose_name=u"Usuário")

    class Meta:
        verbose_name = u"Postagem reportada"
        verbose_name_plural = u"Postagens reportadas"