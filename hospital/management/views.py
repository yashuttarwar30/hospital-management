from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import UserProfile
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# username admin
# password=same as my all,29@abcdef
# Create your views here.


def login(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('f_pass')
        user = auth.authenticate(username=username, password=password)
        if user is not None :
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'management/login.html', {'message': 'Invalid Credentials.'})
    else:
        return render(request,'management/login.html')


def signup(request):
    if request.method == "POST":


        username = request.POST.get("username")
        print(username)
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        f_pass = request.POST.get("f_pass")
        c_pass = request.POST.get("c_pass")

        if c_pass == f_pass:
            try:
                user = User.objects.get(username=username)
                return render(request, 'management/signup.html', {'message': 'User Already Exist.'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=f_pass)
                user.save()
                profile = UserProfile(user=user, phone=int(phone))
                profile.save()









                return HttpResponseRedirect('login')
        else:
            return render(request,'management/signup.html',{'message' : 'password not matching'})
    else:


            return render(request, 'management/signup.html')


def index(request):
    if request.method=='POST':

        return render(request, 'management/index.html')
    else:
        return render(request, 'management/index.html')








































