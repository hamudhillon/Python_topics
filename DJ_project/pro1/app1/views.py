from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request,url):
    baseurl='https://images.pexels.com/photos/'
    url=f"{url}/pexels-photo-{url}.jpeg"
    print(baseurl+url)
    return render(request,'index.html',{
        'image':baseurl+url
    })
def add(request,n1,n2):
    return HttpResponse(f'<h2>{n1+n2}</h2>')