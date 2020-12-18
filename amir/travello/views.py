from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import destination,newspost

from django.contrib.auth.decorators import login_required
from django.contrib import redirects
from .models import destination
from django.http import HttpResponse
from .forms import DestinationForm
# Create your views here.

def analyzer(request):
   #get the text
   djtext=request.GET.get('text','default')
   print(djtext)
   #get the check value
   removepunc=request.GET.get('check','off')
   caps=request.GET.get('caps','off')
   rmvnwline=request.GET.get('rmvnwline','off')
   spaceremove=request.GET.get('spaceremove','off')
   chcount=request.GET.get('chcount','off')
   
   #analyze the text
   punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
   analyzed_text=''
   if removepunc=='on':
      for ch in djtext:
         if ch not in punctuations:
            analyzed_text+=ch
      return render(request,'analyze.html',{'purpose':'Remove Punctuation','analyzed':analyzed_text})
   elif caps=='on':
      for ch in djtext:
         analyzed_text+=ch.upper()
      return render(request,'analyze.html',{'purpose':'CAPITALIZED','analyzed':analyzed_text})

   elif rmvnwline=='on':
      for ch in djtext:
         if ch!='/n':
            analyzed_text+=ch
      return render(request,'analyze.html',{'purpose':'Removed new lines','analyzed':analyzed_text})

   elif spaceremove=='on':
      for index,ch in enumerate(djtext):
         if not(djtext[index]==" " and djtext[index+1]==" "):
            analyzed_text+=ch
      return render(request,'analyze.html',{'purpose':'Removed spaces','analyzed':analyzed_text})
   
   elif chcount=='on':
     c=0
     for ch in djtext:
        if (ch!=' '):
           c+=1
     return render(request,'analyze.html',{'purpose':'Characters counted','analyzed':c})

      
      
      
   else:
      return HttpResponse("error")

def nav(request):
   pass
#    navs="<h1>personal navigation bar>/h1>
#    <a href=''
#    "
#    return HttpResponse()

def home(request):
   return redirect('/')

def page1(request):
   # return HttpResponse("<h1>page 1</h1> <a href='home'>go to home</a> ")
   return render(request,'textutils.html')

def series(request):
   return HttpResponse("<h1>series</h1> <a href='https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9'>watch harry's series</a>")

def page3(request):
   return HttpResponse("<h1>page 3</h1> <a href='home'>go to home</a>")


def search(request):
   if request.method=='POST':
      city=request.POST['city']
      
     
      if destination.objects.filter(name=city).exists():
         dept=request.POST['dept']
         ariv=request.POST['ariv']
         


         return HttpResponse('working search'+city)
      else:
         return HttpResponse(city+' not found')

def destinations(request,dest_id):
     if request.user.is_authenticated:
        dest=get_object_or_404(destination,pk=dest_id)
        print(dest)
        
        return render(request,'destinations.html',{'dests':dest})
     else:
        return redirect('login')

# @login_required
# def destinations(request,dest_id):
#    dest=get_object_or_404(destination,pk=dest_id)
#    return render(request,'destinations.html',{'dests':dest})
   

def tell(request):
   return HttpResponse("<h1>telling...</h1>")

   
def index(request):
    # dest1=destination()
    # dest1.price=700
    # dest1.desc='City of Joy'
    # dest1.name='KOLKATA'
    # dest1.img='KOLKATA.jpg'
    # dest1.offer=True
    # dest2=destination()
    # dest2.name="MUMBAI"
    # dest2.price=800
    # dest2.desc="city that never sleeps"
    # dest2.img='MUMBAI.jpg'
    # dest2.offer=True
    
    # dest3=destination()
    # dest3.img='nj.jpg'

    # dest3.name="NEW JERSEY"
    # dest3.price=900
    # dest3.desc="Heaven in America"
    # dest3.offer=False

    # for newspost
   #  news1=newspost()
   #  news1.date="02"
   #  news1.month="JUN"
   #  news1.text="travel more and enjoy"
   #  news1.title="Best tips to travel"
   #  news2=newspost()
   #  news2.date="02"
   #  news2.month="MAY"
   #  news2.text="travel more and enjoy"
   #  news2.title="Best tips to travel"
   #  news3=newspost()
   #  news3.date="03"
   #  news3.month="JUN"
   #  news3.text="travel more and enjoy"
   #  news3.title="Best tips to travel"

   #  news4=newspost()
   #  news4.month="JUN"
   #  news4.text="travel more and enjoy"
   #  news4.title="Best tips to travel"
   #  news4.date="04"

    

    # dests=[dest1,dest2,dest3]
    dests=destination.objects.all()
    newsposts=newspost.objects.all()
    
    
    return render(request,'index.html',{'dests':dests,'newspost':newsposts})

def destination_create(request):
   form=DestinationForm(request.POST    or None)
   name=request.POST.get('name')
   desc=request.POST.get('desc')
   
   if form.is_valid:
      instance=form.save(commit=False)
      instance.save()
   return render(request,'destination_form.html',{'form':form})

def about(request):
   return HttpResponse("about")