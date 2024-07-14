from django.core.management.base import BaseCommand
from ...models import User

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users = User.objects.all()
        self.stdout.write(f'{users}')