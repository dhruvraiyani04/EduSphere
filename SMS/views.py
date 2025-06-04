from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, logout, login
from app.EmailBackEnd import EmailBackEnd
from django.contrib import messages
from app.models import CustomUser
from django.contrib.auth.decorators import login_required

def BASE(request):
    return render(request, 'base.html')

def LOGIN(request):
    return render(request, 'login.html')

def doLogout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/')
def PROFILE(request):
    user = CustomUser.objects.get(id = request.user.id)
    context = {
        "user":user,
    }
    print(user)
    return render(request,'profile.html',context)

@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        try:
            customuser = CustomUser.objects.get(id = request.user.id)

            customuser.first_name = first_name
            customuser.last_name = last_name

            if password !=None and password != "":
                customuser.set_password(password)
            if profile_pic !=None and profile_pic != "":
                customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request,'Your Profile Updated Successfully !')
            return redirect('profile')
        except:
            messages.error(request,'Failed To Update Your Profile')

    return render(request,'profile.html')

def doLogin(request):
    if request.method == 'POST':
        username = request.POST.get('email')  # Use lowercase 'email'
        password = request.POST.get('password')
        print(f"Username: {username}, Password: {password}")  # Debug print

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print(f"User {user} authenticated successfully.")
            login(request, user)
            User_type = user.User_type
            if User_type == '1':
                return redirect('hod_home')
            elif User_type == '2':
                return redirect('staff_home')
            elif User_type == '3':
                return redirect('student_home')
            else:
                messages.error(request, "User type not recognized.")
                return redirect('login')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
    else:
        messages.error(request, "Invalid request method.")
    return redirect('login')
