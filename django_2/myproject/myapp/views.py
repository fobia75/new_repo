from django.shortcuts import render
from random import choice
from django.http import HttpResponse
from .models import Coin

def index(request):
    return HttpResponse('hello world')


def coin(request):
    site = choice(['орел','решка'])
    arg_coin = Coin(site= site)
    arg_coin.save()
    return HttpResponse(str(site))


def coin_v(request):
    caunt = Coin.value_coin()
    print(caunt)
    dict_c= []
    for i in caunt:
        print(i)
        dict_c.append(i.site)
    return HttpResponse(dict_c)

#
