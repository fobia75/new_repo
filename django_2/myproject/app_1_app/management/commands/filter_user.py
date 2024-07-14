from django.core.management.base import BaseCommand
from ...models import User

class Command(BaseCommand):
    help = 'filter user by id'


    def add_arguments(self, parser):
        parser.add_argument('pk', type= int, help= 'user id')


    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.filter(pk = pk).first() 
        self.stdout.write(f'{user}')      