from django.urls import path

from .views import index,names
urlpatterns = [
    path('welcome/<int:id>',index,name='index'),
    path('names/<str:fname>/<str:lname>',names)
]
