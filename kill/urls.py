from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('del',views.Delete_task.as_view(),name='delete')
]