from django.shortcuts import render
from .models import *


def index(request):
    categoriya = Categoriya.objects.all()

    ctx = {
        'categoriya': categoriya
    }

    return render(request, 'main/index.html', ctx)



def pro(request, id):
    product = Product.objects.filter(categoriya_id=id)
    ctx = {
        "product": product
    }

    return render(request, 'main/pro.html')





