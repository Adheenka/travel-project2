from . import views
from django.urls import path

urlpatterns = [

    path('',views.dummy,name='dummy'),
]
