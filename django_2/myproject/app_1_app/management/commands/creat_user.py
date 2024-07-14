from django.core.management.base import BaseCommand
from ...models import User


class Command(BaseCommand):
    help = "create user"


    def handle(self, *args, **kwargs):
        user = User(name= 'mic', email = 'jon@mail.ru', password = 'sekret', age = 35)
        user.save()
        self.stdout.write(f'{user}')


      