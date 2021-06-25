from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import *


# class HomeView(ListView):
#     model = Post
#     template_name = "home.html"


class AboutView(TemplateView):
    template_name = 'about.html'



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "home.html", context)