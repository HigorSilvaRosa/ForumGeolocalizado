# coding=utf-8
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render_to_response, redirect
from django.contrib import messages
from django.template.context import RequestContext
from django.views.generic.base import View
from core.models import Topic, Post

class TopicView(View):
    def get(self, request, topic_id,  *args, **kwargs):
        page_template = "site/topic.html"
        page_data = {}
        try:
            user_coordinates = request.session["coordinates"]
        except:
            user_coordinates= None
        if user_coordinates:
            page_data["coordinates"] = {
                "latitude": str(request.session["coordinates"][0]).replace(',', '.'),
                "longitude": str(request.session["coordinates"][1]).replace(',', '.'),

                }
        topic = Topic.objects.get(id=topic_id)
        page_data['topic'] = topic
        return render_to_response(page_template, page_data, RequestContext(request))
    def post(self, request, topic_id,  *args, **kwargs):
        post = Post(
            topic_id=topic_id,
            user=request.user,
            content=request.POST.get("content")
        )
        post.save()
        return redirect("topic", topic_id)

class HomeView(View):
    def get(self, request,  *args, **kwargs):
        page_template = "site/home.html"
        page_data = {}
        try:
            user_coordinates = request.session["coordinates"]
        except:
            user_coordinates= None
        if user_coordinates:
            page_data["coordinates"] = {
                "latitude": str(request.session["coordinates"][0]).replace(',', '.'),
                "longitude": str(request.session["coordinates"][1]).replace(',', '.'),

                }
        return render_to_response(page_template, page_data, RequestContext(request))

class LoginView(View):
    def post(self, request,  *args, **kwargs):
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
            else:
                messages.error(request, u"Sinto muito, mas esse usuário está desativado atualmente.")
        else:
            messages.error(request, u"Usuário ou senha inválidos.")
        return redirect("home")

class LogoutView(View):
    def get(self, request,  *args, **kwargs):
        logout(request)
        return redirect("home")

class CreateTopicView(View):
    def post(self, request,  *args, **kwargs):
        latitude = request.session['coordinates'][0]
        longitude = request.session['coordinates'][1]
        topic = Topic(latitude=latitude, longitude=longitude, user=request.user, name=request.POST.get("name", None))
        topic.save();
        return redirect("topic", topic.id)