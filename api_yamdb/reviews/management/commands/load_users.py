from django.core.management import BaseCommand
from users.models import User

from ._loader import data_loader


class Command(BaseCommand):
    def handle(self, *args, **options):
        data_loader(User, 'users.csv')
