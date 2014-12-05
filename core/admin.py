from django.contrib import admin

# Register your models here.
from django.contrib.admin.options import ModelAdmin
from core.models import Topic, Post, UserCoordinates

class UserCoordinatesAdmin(ModelAdmin):
    list_display = ("id", "latitude", "longitude", "user")

admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(UserCoordinates, UserCoordinatesAdmin)