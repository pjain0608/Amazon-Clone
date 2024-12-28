from django.urls import path
from . import views

urlpatterns = [
    path('1',views.mx_player, name = 'mx_player'),
]