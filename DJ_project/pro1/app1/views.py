from django.shortcuts import render
from django.http import HttpResponse

from .models import blogpost

# Create your views here.


def index(request,url):
    # baseurl='https://images.pexels.com/photos/'
    # url=f"{url}/pexels-photo-{url}.jpeg"
    # print(baseurl+url)
    context={}
    userdata=[
        {
            'Name':'Harman',
            'Phone':3456789,
            'Age':56
        },
        {
            'Name':'asjdhkj ',
            'Phone':32767,
            'Age':18
        }
        ,{
            'Name':'Harmaasdjakn',
            'Phone':213214,
            'Age':11
        },
        {
            'Name':'Haksdhjkaarman',
            'Phone':324324,
            'Age':32
        }
        ,{
            'Name':'askdhHarman',
            'Phone':3456789,
            'Age':12
        }
    ]


    context.update({'users':userdata})
    context.update({'p':'''Commodi odit modi, minus pariatur in veniam rem iste exercitationem quasi
      suscipit beatae accusamus. Ad dolor ducimus doloribus omnis corporis ipsa
      obcaecati optio suscipit, nobis ex id sequi similique. Veritatis amet
      architecto nemo quisquam voluptates earum beatae, cumque amet omnis?
      Perferendis iure esse eum veritatis minima ea laudantium tempora fugit
      dolorum? Commodi odit modi, minus pariatur in veniam rem iste
      exercitationem quasi suscipit beatae accusamus. Ad dolor ducimus doloribus
      omnis corporis ipsa obcaecati optio suscipit, nobis ex id sequi similique.
      Veritatis amet architecto nemo quisquam voluptates earum beatae, cumque
      amet omnis? Perferendis iure esse eum veritatis minima ea laudantium
      tempora fugit dolorum? Commodi odit modi, minus pariatur in veniam rem
      iste exercitationem quasi suscipit beatae accusamus. Ad dolor ducimus
      doloribus omnis corporis ipsa obcaecati optio suscipit, nobis ex id sequi
      similique. Veritatis amet architecto nemo quisquam voluptates earum
      beatae, cumque amet omnis? Perferendis iure esse eum veritatis minima ea
      laudantium tempora fugit dolorum?'''})
    return render(request,'index.html',context)
def add(request,n1,n2):
    return HttpResponse(f'<h2>{n1+n2}</h2>')

def about(request):
    
    return render(request,'about.html',{})

def create(request):
    
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        image=request.FILES['image']
        cat=request.POST['cat']
        postby=request.POST['postBy']
        print(title,desc,image,cat,postby)

        ob=blogpost()
        ob.title=title
        ob.desc=desc
        ob.image=image
        ob.post_by=postby
        ob.category=cat
        ob.save()

    return render(request,'Createpost.html',{})


def allpost(request):
    # ob=blogpost.objects.get(id=2) #for one row
    ob=blogpost.objects.all() #for all rows

    return render(request,'allpost.html',{'data':ob})