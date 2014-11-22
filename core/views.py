from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.template.context import RequestContext
from django.views.generic.base import View
from core.models import Topic, Post


class TopicView(View):
    def get(self, request, topic_id,  *args, **kwargs):
        page_template = "site/topic.html"
        page_data = {}
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

class LoginView(View):
    def get(self, request,  *args, **kwargs):
        page_template = "site/login.html"
        page_data = {}
        return render_to_response(page_template, page_data, RequestContext(request))