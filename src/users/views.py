from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from users.forms import LoginForm, RegisterForm


def loginView(request):
    form = LoginForm()
    error = None

    if request.user.is_authenticated:
        return redirect('web:home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        next_rd = request.GET.get('next')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_rd is None:
                return redirect('web:home')
            else:
                return redirect(next_rd)
        else:
            error = 'کاربر با نام کاربری و رمز عبور زیر یافت نشد!'
    return render(request, 'login.html', {"form": form, "error": error})


def registerView(request):
    form = RegisterForm()
    error = None

    if request.user.is_authenticated:
        return redirect('web:home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('web:home')
        else:
            error = 'خطا در اطلاعات ورودی!'

    return render(request, 'register.html', {"form": form, "error": error})


def logoutView(request):
    logout(request)
    return redirect('web:home')
