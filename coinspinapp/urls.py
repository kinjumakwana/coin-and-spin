from django.urls import path
from .views import *

urlpatterns = [
    path('', index ,name="index"),
    # path('add_post/<str:detail>/<str:link>/<str:title>/',add_post, name='add_post'),
    path('add_post/',add_post ,name="add_post"),
]
