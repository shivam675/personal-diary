from django.shortcuts import render
from log.forms import LogForm

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError 
from django.contrib.auth import login, logout, authenticate
from .forms import LogForm
from .models import MyLogEntry
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'signupuser.html', {'form': UserCreationForm()})
    else: 
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signupuser.html', {'form': UserCreationForm(), 'error': 'Username already taken.'})
        else: 
            return render(request, 'signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords do not match.'})

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'loginuser.html', {'form': AuthenticationForm()})
    else: 
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'loginuser.html', {'form': AuthenticationForm(), 'error': 'username and password did not match our records.'})
        else:
            login(request, user)
            return redirect('home')

def home(request):
    return render(request, 'home.html')


@login_required
def create_log(request):
    tim = timezone.now()
    if request.method == 'GET':
        return render(request, 'create_log.html', {'form': LogForm(), 'time': tim})
    else:
        try:
            form = LogForm(request.POST)
            new_log = form.save(commit=False)
            new_log.user = request.user
            new_log.save()
            # print(new_log.id)
            # print(new_log.created)
            return redirect('home')
        except ValueError:
            return render(request, 'create_log.html', {'form': LogForm(), 'error': 'Invalid data types and/or character limit exceeded.'})


@login_required
def view_logs(request, log_pk):
    log = get_object_or_404(MyLogEntry, pk=log_pk, user=request.user)
    if request.method =='GET':
        form_main = LogForm(instance=log)
        return render(request, 'view_log.html', {'log': log, 'form': form_main})
    else: 
        form_main = LogForm(request.POST, instance=log)
        if form_main.is_valid():
            print('Data is good')
        else:
            print()
        form_main.save()
        return redirect('home')


@login_required
def view_all_logs(request):
    # all_objects = MyLogEntry.__class__.objects.all()
    all_objects = MyLogEntry.objects.all()
    all_objects = list(all_objects)
    decent_list = []
    for idx in range(0, len(all_objects), 3):
        # print(idx)
        decent_list.append(all_objects[idx:idx+3])
    print(decent_list)
    return render(request, 'all-logs.html', {'decent_list': decent_list})



@login_required
def delete_logs(request, log_pk):
    todo = get_object_or_404(MyLogEntry, pk=log_pk, user=request.user)
    if request.method == 'POST' and todo.user == request.user:
        todo.delete()
        return redirect('home')