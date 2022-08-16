from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request,id):
    if id==1:
        name='Random'
    elif id==2:
        name='Shaam'
    context={
        'User':name
    }
    return render(request,'index.html',context)

def names(request,fname,lname):

    fullname=fname+' '+lname
    return HttpResponse(fullname)