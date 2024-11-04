from django.shortcuts import render, redirect
from .forms import RegisterForm, TimeEntryModelForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import TimeEntryModel


def index(request):
    context = {}
    return render(request, 'app/index.html', context)


@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, 'app/home.html', context)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                print("@@@ VALID - User successfully created & saved to database")
                username = form.cleaned_data.get('username')
                messages.success(request, username)
                return redirect('login')

        else:
            form = RegisterForm()

        context = {'form': form}
        return render(request, 'app/register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                full_name = request.user.get_full_name()
                messages.success(request, full_name)
                return redirect('home')
            else:
                print("### Incorrect Credentials ! ###")
                messages.warning(request, "Username or Password is incorrect")
                return redirect('login')

        else:
            return render(request, 'app/login.html')


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.info(request, "Logged Out Successfully ! Das Vedanya !")
    return redirect('login')


@login_required(login_url='login')
def time_entry_create(request):
    if request.method == 'POST':
        # print(request.POST)
        form = TimeEntryModelForm(request.POST)

        if form.is_valid():
            form.save()
            print("@@@ VALID - Time-Entry successfully created & saved to database")
            developer = form.cleaned_data.get('dev')
            messages.success(request, developer)
            return redirect('time_entry')

    else:
        form = TimeEntryModelForm()

    context = {'form': form}
    return render(request, 'app/time_entry_create.html', context)


class TimeEntryModelList(ListView):
    model = TimeEntryModel
