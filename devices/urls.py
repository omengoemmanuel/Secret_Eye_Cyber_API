from django.urls import path
from . import views

urlpatterns = [
    path('dataview', views.viewdata),
    path('add', views.add),
    path('adddata1', views.adddata1)
]
