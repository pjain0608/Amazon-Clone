from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'amazon'),
    path('1',views.fresh, name = 'fresh'),
    path('2',views.sell, name = 'sell'),
    path('3',views.best_seller, name = 'best_seller'),
    path('4',views.today_deal, name = 'today_deal'),
    path('5',views.home_kitchen, name = 'home_kitchen'),
    path('6',views.customer_service, name = 'customer_service'),
    path('7',views.prime, name = 'prime'),
]
