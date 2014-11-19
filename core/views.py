from django.shortcuts import render, render_to_response

# Create your views here.
from django.template.context import RequestContext
from django.views.generic.base import View


class TopicView(View):
    def get(self, request, *args, **kwargs):
        page_template = "site/topic.html"
        page_data = {}
        return render_to_response(page_template, page_data, RequestContext(request))