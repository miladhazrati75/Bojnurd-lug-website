from django.shortcuts import render, HttpResponse
from .models import Post


def index(request):
    return render(request, 'index.html', {'posts': Post.objects.all()})
