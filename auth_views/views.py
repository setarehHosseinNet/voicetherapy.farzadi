from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # کاربر را بعد از ثبت‌نام وارد سیستم می‌کند
            return redirect('home')  # به صفحه اصلی هدایت می‌شود
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
