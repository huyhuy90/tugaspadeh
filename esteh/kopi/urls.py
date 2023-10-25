from django.urls import path
from . import views

urlpatterns = [
    path('kopi/', views.kopi, name='kopi'),
]