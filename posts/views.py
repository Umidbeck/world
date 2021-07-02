from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import *
from django.shortcuts import *


# class HomeView(ListView):
#     model = Post
#     template_name = "home.html"


class AboutView(TemplateView):
    template_name = 'about.html'



def home(request):
    context = {
        'posts': PostModel.objects.all(),
        'category': CategoryModel.objects.all()
    }
    return render(request, "home.html", context)




def create(request):
    if request.method == "POST":
        p= PostModel(title=request.POST['title'], text=request.POST['text'])
        p.save()
        return redirect("home")

    return render(request, "create.html")


def update(request, id):
    try:
        p = PostModel.objects.get(id=id)
    except PostModel.DoesNotExist:
        return redirect("home")

    if request.method == "POST":
        p.title =request.POST['title']
        p.text = request.POST['text']
        p.save()

        return redirect("home")

    return render(request, "create.html", {
        "p": p
    })


def delete(request, id):
    PostModel.objects.filter(id=id).delete()
    return redirect("home")