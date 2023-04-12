from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
# from coinspinapp.main import Facebookboat

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
    
# def add_post(request):
#     # fb = Facebookboat
#     # fb.login()
#     # addpost = Coinmaster.objects.create(title="",detial="",link="")
#     # addpost.save()
#     # print(addpost)
#     print("Successfully added")
#     return render(request,"index.html")