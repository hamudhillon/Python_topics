from django.urls import path
from .views import *


urlpatterns = [
    path('index/image/<slug:url>',index,name='index'),
    path('add/<int:n1>/<int:n2>',add,name='sum'),
    path('about',about,name='about'),
    path('createpost',create,name='create')
]
