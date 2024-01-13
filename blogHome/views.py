from django.shortcuts import render,HttpResponse,redirect
from . models import Blog,Comment,Reply
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User
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
    comment=Comment.objects.all().order_by("-id")
    reply=Reply.objects.all()
    context={
        'blog':blog,
        'comment':comment,
        'reply':reply
    }
    return render(request,'blogcontent.html',context)


from django.contrib.auth.models import User
from django.http import HttpResponse

def signup(request):
    if request.method == 'POST':
        fname = request.POST.get("fname")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not fname:
            # Handle the case where the first name is not provided
            # Return an HttpResponse with the error message
            error_message = "Please provide a first name."
            return HttpResponse(error_message)

        # Create the user with the provided information
        user = User.objects.create_user(first_name=fname, username=email, email=email, password=password)
        user.save()
        return redirect('Home')

    return render(request, 'signup.html')



def Login(request):
        if request.method == 'POST': 
            
            email= request.POST.get("email")
            password= request.POST.get("password")
            user = authenticate(request, username=email, password=password)
            print(user)
            if user is not None:
                messages.info(request,"successfully login")
                login(request, user)
            else:
                messages.error(request,"Invalid credentials")
            return redirect('Home')
            
        return render(request,'login.html')
    
    
def logout_view(request):
    logout(request)
    return redirect('Home')
        
        
def comment(request):
    if request.method == "POST":
        name = request.user
        blog_id=request.POST.get('blogid')
        comment=request.POST.get('comment')
        
        blog=Blog.objects.get(id=blog_id)
        comment = Comment(name=name,blogparent=blog,comment=comment)
        comment.save()
        
        messages.success(request,"Comment succeesfully added")
        
    return redirect(f"content/{blog_id}")


def replies(request):
    if request.method =='POST':
        name=request.user
        blog_id=request.POST.get('blogid')
        commentparent=request.POST.get('commentparent')
        reply=request.POST.get("reply")
        
        print(name,commentparent,reply)
        comment=Comment.objects.get(id=commentparent)
        replied= Reply(name=name,commentparent=comment,reply=reply)
        replied.save()
        messages.success(request,"Reply added")
    
    return redirect(f"content/{blog_id}")