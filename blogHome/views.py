from django.shortcuts import render,HttpResponse
from . models import Blog
# Create your views here.
def home(request):
    blog = Blog.objects.all() 
    context={
        'blog': blog
    }
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def content(request,id):
    blog=Blog.objects.get(id=id)
    
    context={
        'blog':blog
    }
    return render(request,'blogcontent.html',context)