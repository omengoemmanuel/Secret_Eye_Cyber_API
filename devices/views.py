from django.shortcuts import render
from .serializer import shopserializer
from .models import shop
from rest_framework import viewsets


# Create your views here.
class shopview(viewsets.ModelViewSet):
    queryset = shop.objects.all()
    serializer_class = shopserializer


def viewdata(request):
    view1 = shop.objects.all()
    return render(request, 'viewdata.html', {'view1': view1})
