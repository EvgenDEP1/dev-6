from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from mainapp.models import Photo
import random


@login_required()
def index(request):
    num_img = Photo.objects.all()
    random_img = random.choices(num_img)
    context = {
        'title': 'главная',
        'num_img': random_img,
    }
    return render(request, 'mainapp/index.html', context)
