from django.urls import path
from . import views
urlpatterns = [
    path('dataview', views.viewdata)

]