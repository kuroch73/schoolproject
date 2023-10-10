from sqlite3 import IntegrityError

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User

from .models import Student
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
   return render(request, 'testapp/home.html')

def Studentlist(request):
    students = Student.objects.all()
    return  render(request, 'testapp/Studentlist.html', context={ 'students' : students})


def loginStudent(request):
    return render(request, 'testapp/login.html')

def goalsList(request):
   return render(request, 'testapp/goals.html')

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username , password= password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'testapp/login.html', {'form': form})
def reguserView(request):
    if request.method == "GET":
        return render(request, 'testapp/reguser.html', {'formuser' : UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'testapp/reguser.html', {'formuser': UserCreationForm(), 'error': 'Это имя уже используется'})
        else:
            return render(request, 'testapp/reguser.html', {'formuser': UserCreationForm(), 'error': 'Пароль не совпадает'})