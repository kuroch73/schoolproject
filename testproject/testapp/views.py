from django.shortcuts import render
from .models import Student

# Create your views here.
def index(request):
   return render(request, 'testapp/home.html')


def about(request):
    return render(request, 'testapp/about.html')

def Studentlist(request):
    students = Student.objects.all()
    return  render(request, 'testapp/Studentlist.html', context={ 'students' : students})

def hello_world(request):
    message = "Hello world"
    return render(request, 'hello')