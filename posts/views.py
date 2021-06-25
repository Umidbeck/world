from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import *
from django.shortcuts import redirect


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




def create(request):
    if request.method == "POST":
        p= Post(title=request.POST['title'], text=request.POST['text'])
        p.save()
        return redirect("home")

    return render(request, "create.html")


def update(request, id):
    try:
        p = Post.objects.get(id=id)
    except Post.DoesNotExist:
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
    Post.objects.filter(id=id).delete()
    return redirect("home")