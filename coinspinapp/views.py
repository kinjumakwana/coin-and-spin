from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
# from coinspinapp.main import Facebookboat
from django.views import View
from firebase_admin import firestore

# Create your views here.
def index(request):
    return render(request,"index.html")

@csrf_exempt
def add_post(request):
    detail = request.POST.get('detail')
    link = request.POST.get('link')
    title = request.POST.get('title')
    post_data = {
        'detail': detail,
        'link': link,
        'title': title,
    }
    post = Coinmaster.objects.create(**post_data)
    post.save()
    print("Successfully added")
    return render(request, 'index.html', {'post': post})
    # post = Coinmaster.objects.create(detail=detail, link=link, title=title)
