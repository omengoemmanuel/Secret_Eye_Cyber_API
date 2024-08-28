from django.shortcuts import render, redirect
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


def add(request):
    return render(request, 'add.html')


def adddata1(request):
    if request.method == "POST":
        Device_Name = request.POST.get('Device_Name')
        Device_Colour = request.POST.get('Device_Colour')
        Model_Number = request.POST.get('Model_Number')
        Manufacturer = request.POST.get('Manufacturer')

        if len(request.FILES) != 0:
            Device_Photo = request.FILES['Device_Photo']
        query = shop(Device_Name=Device_Name, Device_Colour=Device_Colour, Model_Number=Model_Number, Manufacturer=Manufacturer, Device_Photo=Device_Photo)
        query.save()

        return redirect('/add')
    return redirect('/add')




