from django.urls import path

from .views import index

urlpatterns = [
    path('welcome',index,name='index'),
]
