from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect



from django.contrib import auth



from django.urls import reverse

from authapp.forms import LoginForm



# @login_required()
def index(request):
    # context = {
    #     'title': 'главная',
    # }
    return render(request, 'mainapp/index.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        form = LoginForm()

    context = {
        'form': form,
        'page_title': 'авторизация',
    }
    return render(request, 'registration/login.html', context)