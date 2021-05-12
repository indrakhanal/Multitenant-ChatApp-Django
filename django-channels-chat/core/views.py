
from django.shortcuts import render, redirect
from chat.forms import SignUpForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    return render(request, 'core/chat.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'core/chat.html')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


# @login_required(login_url='login')
def logout_(request):
    logout(request)
    return redirect('login')


def login_(request):
    try:
        if request.method == 'GET':
            return render(request, 'registration/login.html')
        else:
            u = request.POST.get('username')
            p = request.POST.get('password')
            user = authenticate(username=u, password=p)
            if user is not None:
                login(request, user)
                # return redirect('home')
                return render(request, 'core/chat.html')

            else:
                message = 'username or password not correct'
                return render(request, 'registration/login.html', {'errors':message})
    except:
        error_message = 'Something went wrong please retry'
        return render(request, 'registration/login.html', {'errors':error_message})

