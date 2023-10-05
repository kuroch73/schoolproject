from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
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