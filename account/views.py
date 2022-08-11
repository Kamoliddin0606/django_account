from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import UserChangeForm
from .forms import Editprofile
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request=request, template_name='account/index.html')
    else:
        return redirect('login')

def login_view(request):
    if request.method == 'POST':
        userreq = request.POST.get('username')
        password = request.POST.get('password')
        print(userreq)
        print(password)
        user = authenticate(username= userreq, password=password)
        print(user)
        if user is not None:
            login(request=request, user=user)
            return redirect('index')
            

    return render(request, 'registration/login.html')
def logout_view(request):
    logout(request=request)
    return redirect('index')
def change_pas(request):
    if request.method =='POST':
        hashPass = request.user.password
        passwordOld = request.POST.get('password')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if check_password(passwordOld, hashPass):
            if password1==password2:
                request.user.set_password(password2)
                request.user.save()
                return redirect('login')
    return render(request=request, template_name='registration/changepass.html')

def createuser(request):
    form  =UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context={
        'form':form
    }
    return render(request=request, template_name='registration/create.html', context=context)

def editProfile(request):
    form =Editprofile(instance=request.user)
    print(form)
    if request.method == 'POST':
        form = Editprofile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
            
    context = {
        'form':form
    }
    return render(request=request, template_name='account/editprofile.html', context=context)