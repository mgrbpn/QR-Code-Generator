from django.shortcuts import render
from django.conf import settings
from qrcode import *
import random

# Create your views here.
def index(request):
    if request.method == "POST":
        Url = request.POST['url']
        img = make(Url)
        img_name = f'qrimg{random.randint(1, 1000)}.png'
        img.save(settings.MEDIA_ROOT/img_name)
        return render(request, "index.html", {'img': img_name})
    return render(request, "index.html")
    
