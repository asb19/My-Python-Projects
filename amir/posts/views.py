from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.http import HttpResponseRedirect,Http404
from .models import posts
from django.contrib.auth.forms import UserCreationForm
from .forms import PostForm
from django.core.paginator import Paginator
from django.shortcuts import render
from urllib.parse import quote_plus
from django.contrib import auth
from django.contrib.auth.decorators import login_required





# Create your views here.
@login_required
def post_list(request):
    user=request.user
    # items_list=user.posts_set.all()
    items_list=posts.objects.all().order_by('-updated')
    paginator = Paginator(items_list, 8) # Show 25 contacts per page
    page = request.GET.get('page')
    items = paginator.get_page(page)
    
    return render(request,'posts/posts.html',{'posts':items,'title':'Lists','cur_user':request.user})


   
def post_detail(request,slug):
    item=get_object_or_404(posts,slug=slug)
    details=item
    shared_string=quote_plus(item.content)

    return render(request,'posts/post_detail.html',{'details':item,'shared_string':shared_string})
def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    
    
    form=PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        
        instance.user=request.user
        user1=instance.user
        print(instance.user)
        instance.save()
        
        return HttpResponseRedirect(instance.get_absolute_url())

    create_form=PostForm()
    return render(request,'posts/post_form.html',{'form':create_form})
def post_update(request,slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance=get_object_or_404(posts,slug=slug)
    form=PostForm(request.POST or None,request.FILES or None,instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"item updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    create_form=form
    return render(request,'posts/post_form.html',{'form':create_form})

def post_delete(request,id):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    item=get_object_or_404(posts,id=id)
    item.delete()
    return HttpResponseRedirect("/posts")

# def post_login(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']

#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('/posts')
#         else:
#             messages.info(request,'invalid credentials')
#             return redirect('login')
#     else:
#         return render(request,'posts/post_login.html')

# def post_register(request):
#     if request.method=='POST':
#         first_name=request.POST['first_name']
#         last_name=request.POST['last_name']
#         username=request.POST['username']
#         email=request.POST['email']
#         password1=request.POST['password1']
#         password2=request.POST['password2']
#         if password1==password2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,'user already exists')
#                 return redirect('register')
#             elif User.objects.filter(email=email):
#                 messages.info(request,'email exists')
#                 return redirect('register')
                
#             else:
#                 user=User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
#                 user.save()
#                 print('user created')
#                 return redirect('login')
#         else:
#             messages.info(request,'password did not match')
#             return redirect('register')
#         return redirect('/posts')
                


#     else:
#         return render(request,'posts/post_register.html')

# def post_logout(request):
#     auth.logout(request)
#     return redirect('posts')



   
