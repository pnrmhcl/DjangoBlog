from django.shortcuts import render
from django.views import generic
from pinarblog.models import Post
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User

def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    return render(request,'core/frontpage.html', {'posts': posts})

def about(request):
    return render(request,'core/about.html')

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text),content_type="text/plain")

class CreateUser(generic.CreateView):
    success_url = reverse_lazy("login")

    form_class=UserCreationForm
    queryset= User.objects.all()
    template_name="registration/signup.html"