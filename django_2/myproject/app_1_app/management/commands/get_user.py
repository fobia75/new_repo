from django.core.management.base import BaseCommand
from ...models import User

class Command(BaseCommand):
    help = 'get user by id'

    def add_arguments(self, parser):
        parser.add_argument('id', type= int, help= 'user id')


    def handle(self, *args, **kwargs):
        id = kwargs['id']
        user = User.objects.get(id=id) 
        self.stdout.write(f'{user}')  