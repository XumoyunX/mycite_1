from django.urls import path
from main.views import *


urlpatterns = [
    path('', index, name='index'),
    path('pro/<int:id>/', pro, name='pro')
]
