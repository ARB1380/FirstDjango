from django.shortcuts import render, redirect,reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm #UserCreationForm
from django.contrib.auth.decorators import login_required
from accounts.forms import UserCreationForm #AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
# Create your views here.


def login_view(request):
    msg = ''
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        # print(form.cleaned_data.get('username'))
        # print(form.cleaned_data.get('password'))
        print("enter")

        if form.is_valid():
            print("enter valid")
            username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(username= username, password = password)
            if user is not None:
                login(request, user)
                return redirect('/')
        else:
            msg = 'login unsuccessful!'



    form = AuthenticationForm()
    context = {'form': form, 'msg': msg}

    return render(request, 'accounts/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("enter this section")
            return redirect(reverse('login'))
    form = UserCreationForm()
    context = {'form': form}

    return render(request, 'accounts/signup.html',context)


def password_reset_view(request):
    if request.method == 'POST':
        new_password = request.POST['password1']
        again_password = request.POST['password2']
        if new_password == again_password:
            user = User.objects.get(username=request.POST['username'])
            user.set_password(new_password)
            user.save()
            return redirect('login/')

    return render(request, 'accounts/password-reset.html')

