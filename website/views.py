from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

def home(request):
    records= Record.objects.all()
    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request,username = username,password =password)
        if user is not None:
            login (request,user)
            messages.success(request,'You Have Been Log In!')
            return redirect('home')
        else:
            messages.success(request,'There Was An Error Logging In,Please Try Again....')
            return redirect('home')

    else:
        return render(request,'home.html',{'records':records})



def logout_user(request):
    logout(request)
    messages.success(request,"you have been logout....!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data ['username']
            password = form.cleaned_data ['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'You Have Successfully Registered Welcome!' )
            return redirect('home')

    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})

    return render(request,'register.html',{'form':form})

def customer_record(requeest,pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request,'record.html',{'customer_record':customer_record})
    else:
        messages.success(request,'You must Be Login To View That Page.....' )
        return redirect('home')
  