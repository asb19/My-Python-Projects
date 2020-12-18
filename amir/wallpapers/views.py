from django.shortcuts import get_object_or_404, render,redirect
from .models import Wallpapers
from .forms import WallpaperForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

# Create your views here.

def wallpaper(request):
    items=Wallpapers.objects.all()
    return render(request,'wallpapers/wallpapers_list.html',{'lists':items})
    
def create_wallpaper(request):
    form=WallpaperForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    return render(request,"wallpapers/wallpaper_form.html",{'form':form})
def detail_wallpaper(request,id):
    item=get_object_or_404(Wallpapers,id=id)
    
    return render(request,"wallpapers/wallpaper_detail.html",{'item':item})

def delete_wallpaper(request,id):
    item=get_object_or_404(Wallpapers,id=id)
    item.delete()
    return redirect('list')



