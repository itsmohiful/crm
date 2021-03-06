from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.shortcuts import redirect, render

from .decorators import unauthenticated_user
from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm

# Create your views here.

#user registration
@unauthenticated_user
def register(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user=form.save()
            messages.success(request,'Account was created for ' + username )

            group = Group.objects.get(name='customer')
            #user.groups.add(group)
            group.user_set.add(user)

            return redirect('home')
        
        else:
            form = UserRegisterForm()

    context = {
        'form' : form,

    }
    
    return render(request,'users/register.html',context)



#user login
@unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,f'Successfully Logedin')
            return redirect('home')

        else:
            messages.info(request,'username or password is incorrenct')


    context = {

    }

    return render(request,'users/login.html',context)


#user log out view
def logout_user(request):
    logout(request)
    messages.success(request,f'Successfully Loged Out')
    return redirect('login')


@login_required(login_url='login')
#user profile view
def profile(request):
    return render(request,'users/profile.html')


#profile update
def update_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance = request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        if user_form.is_valid() or profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request,f'your account has been updated')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance = request.user)
        profile_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'user_form' : user_form,
        'profile_form' : profile_form
    }


    return render(request,'users/profile_update.html',context)

