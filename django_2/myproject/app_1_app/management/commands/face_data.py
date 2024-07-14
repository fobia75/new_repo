from django.core.management.base import BaseCommand
from ...models import User, Order, Product

class Command(BaseCommand):
    help = 'face user '


    def add_arguments(self, parser):
        parser.add_argument('count', type= int, help= 'user id')


    def handle(self, *args, **kwargs):
        count = kwargs.get('count') 
        for i in range(count):
            user =  User(name= f'name_{i}', email = f'name_{i}@mail.ru', password = 'sekret', age = {20+i}) 
            user.save()
            # product = Product(name= f'name_{i}', price = int(f'10{i}'), description ='qwerrrttytytuu', image=)
            for j in range(1, count +1):
                order = Order(customer= user, )