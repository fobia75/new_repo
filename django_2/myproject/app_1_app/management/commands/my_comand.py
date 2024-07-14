
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "print'hello world' to uutput"


    def handle(self, *args, **kwargs) -> str | None:
        self.stdout.write('hello world')