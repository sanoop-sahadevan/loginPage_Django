from django.shortcuts import render

# Create your views here.


from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.


def Home(request):
    return render(request, "home.html")

def Signup(request):
    if request.method=="POST":
        username=request.POST["username"]
        pswd=request.POST["password"]
        email=request.POST["email"]
        if User.objects.filter(email=email).exists():
            return HttpResponse("email is already existed")
        else:
            myuser=User.objects.create_user(username,pswd,email)
            myuser.save()
            return redirect("Home")
    return render(request,"signup.html")      


# def Signup(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         pswd = request.POST["password"]
#         email = request.POST["email"]
#         if User.objects.filter(username=username).exists():
#             # return HttpResponse("helo hii")
#             print("hi")
#         else:
#             user = User.objects.create_user(
#                 username=username, password=pswd, email=email)
#             user.save()
#         return redirect(request, "home.html")


def Loginn(request):
    if request.method == "POST":
        username = request.POST["username"]
        pswd = request.POST["password"]
        user = authenticate(username=username, password=pswd)
        if user is not None:
            login(request, user)
            return HttpResponse("successfull")
    # A backend authenticated the credentials
        else:
            return HttpResponse("not user")

    return render(request, "login.html")
