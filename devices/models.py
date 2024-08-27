from django.db import models


# Create your models here.
class shop(models.Model):
    Device_Name = models.CharField(max_length=50, null=False, blank=False)
    colour_choices = [
        ('choose a colour', 'choose a colour'),
        ('black', 'black'),
        ('white', 'white'),
        ('grey', 'grey'),
        ('other', 'other')
    ]
    Device_Colour = models.CharField(max_length=50, null=False, blank=False, choices=colour_choices)
    Model_Number = models.CharField(max_length=28, null=False, blank=False)
    brand = [
        ('choose manufacturer', 'choose manufacturer'),
        ('HP Inc', 'HP Inc'),
        ('Lenovo', 'Lenovo'),
        ('Dell', 'Dell'),
        ('Samsung', 'Samsung'),
        ('Toshiba', 'Toshiba'),
        ('Microsoft', 'Microsoft'),
        ('Apple Inc', 'Apple Inc')
    ]
    Manufacturer = models.CharField(max_length=20, null=False, blank=False, choices=brand)
    Device_Photo = models.ImageField(upload_to='shop/devices', default='shop/devices/device.jpg')

    def __str__(self):
        return self.Device_Name