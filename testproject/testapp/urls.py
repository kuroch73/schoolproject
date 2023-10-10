from django.urls import path
# from . import views
from .views import *
from testapp.views import registration


urlpatterns = [
    path('', index, name='home' ),
    path('Studentlist/', Studentlist, name='Studentlist'),
    path('login/', loginStudent , name='login'),
    path('goals/', goalsList, name='goals' ),
    path('registration/', registration, name='registration'),
    path('reguser/', reguserView, name='reguser')
]
# path ( 'адрес страниц', 'Views', 'имя вызова Views  адреса страницы')