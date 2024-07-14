
from django.shortcuts import render
from random import choice
from django.http import HttpResponse
from .models import Autor
from .forms import AutorForms


def index(request):
    return HttpResponse('hello world')

def viev_autor(request):
    autors= []
    for i in range(1, 10):
        autor = Autor(name= f'name_{i}', second_name = f'second_name_{i}', email = f'email{i}@mail.ru', bio = f'bpografia_{i}', bday = f'2023-11-25')
        autor.save()
        
    return HttpResponse('autor')


def post_autor(request):
    if request.method == 'POST':
        form = AutorForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            second_name = form.cleaned_data['second_name']
            email = form.cleaned_data['email']
            bio = form.cleaned_data['bio']
            bday = form.cleaned_data['bday']
            autor = Autor(name= name, second_name= second_name, email= email, bday= bday, bio= bio)
            autor.save()
            return render(request, 'blog_app/post_autor.html', {'answer': 'автор добавлен'} )  
    else:
        form = AutorForms() 
    return render(request, 'blog_app/post_autor.html', {'form': form} )           


