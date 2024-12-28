from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def fresh(request):
    return render(request,'fresh.html')

def mx_player(request):
    return render(request,'mx_player.html')

def sell(request):
    return render(request,'sell.html')

def best_seller(request):
    return render(request,'best_seller.html')

def today_deal(request):
    return render(request,'today_deal.html')

def home_kitchen(request):
    return render(request,'home_kitchen.html')

def customer_service(request):
    return render(request,'customer_service.html')

def prime(request):
    return render(request,'prime.html')