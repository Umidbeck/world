from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class HomeView(TemplateView):
    model = Post
    template_name = "home.html"


class AboutView(TemplateView):
    template_name = 'about.html'
