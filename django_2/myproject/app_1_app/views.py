from django.shortcuts import render, redirect
from django.http import HttpResponse
import logging
from .forms import UserForm, ProductForm
from .models import User, Product
from django.db.models import Sum

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'index.html')


def mi_wiew(request):
    neim = 'doil'
    context = {'name': neim}
    return render(request, 'index.html', context)


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"] 
            age = form.cleaned_data["age"] 
            password = form.cleaned_data["password"] 
            user = User(name=name, email=email, age=age, password= password)
            user.save()
            message = 'пользователь сохранен'
            logger.info(f'получили{name}, {email}, {age}, {password}')
    else:
        message = 'введите данные'
        form = UserForm()        
    return render(request, 'user_form.html', {'form': form, 'message': message}) 


def product_viev(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            # form.save()
            name = form.cleaned_data["name"]
            price = form.cleaned_data["price"]
            description = form.cleaned_data["description"]
            image = form.cleaned_data["image"]
            quaniti = form.cleaned_data["quaniti"]
            product = Product(name= name, price= price, description= description, quaniti= quaniti, image= image)
            product.save()
            message = 'товар сохранен'
            return redirect('success')
    else:
        form = ProductForm()
        message = 'заполните форму'
    return render(request, 'upload_img.html', {'form' : form, 'message': message})


def success(request):
    return HttpResponse('successfully uploaded')


def total_in_db(request):
    total = Product.objects.aggregate(Sum('quaniti'))
    context = {
        'title':'общеее количество продуктов в базе данных',
        'total': total['quaniti__sum'],
    }
    return render(request, 'total_products.html', context)



