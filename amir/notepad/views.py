from django.shortcuts import render,redirect,get_object_or_404
from .forms import NoteForm

from .models import Note
# Create your views here.

def create_view(request):
    form=NoteForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.instance.user=request.user
        form.save()
        return redirect('list')
    context={'form':form}

    return render(request,'notepad/create.html',context)

def list_view(request):
    notes=Note.objects.all()
    context={'notes':notes}
    return render(request,'notepad/list.html',context)

def delete_view(request,id):
    note_to_delete=Note.objects.filter(pk=id)
    if note_to_delete.exists():
        note_to_delete.delete()
    return redirect('list')

def update_view(request,id):
    updating_instance=get_object_or_404(Note,pk=id)
    form=NoteForm(request.POST or None,request.FILES or None,instance=updating_instance)
    if form.is_valid():
        form.save()
        return redirect('list')

    context={'form':form}

    return render(request,'notepad/create.html',context)
    
