from django.urls import path

import mainapp.views as mainapp

import mainapp.views as registration


app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),

    path('login/', registration.login, name='login'),
]
