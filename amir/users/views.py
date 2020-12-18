from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm


# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('login')
    else:
        form=UserRegistrationForm()
    return render(request,'posts/user_reg.html',{'form':form})

