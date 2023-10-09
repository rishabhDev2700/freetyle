from django.shortcuts import redirect, render
from django.contrib import messages
from authentication.forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User Registered succesfully')
            return redirect('authentication:login')
        messages.error(request,'Invalid form')

    form = CustomUserCreationForm()
    context={'form':form}
    return render(request,'authentication/register.html',context=context)


def login_user(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request=request,user=user)
            messages.success(request,'Logged in successfully')
            return redirect(request,'store:home')
        messages.error(request,'Invalid credentials!')
        return redirect('authentication:login')
    context = {}
    return render(request,'authentication/login.html',context)

def logout_user(request):
    logout(request)
    return redirect('authentication:login')

def update_user(request):
    if request.method=='post':
        form = CustomUserChangeForm()
        if form.is_valid():
            form.save()
            messages.success(request,'Updated user details')
            return redirect('store:update_user')
        messages.error(request,'Invalid details. Please check the data.')

    form = CustomUserChangeForm(instance=request.user)
    context = {'form':form}
    return render(request,'authentication/register.html',context=context)