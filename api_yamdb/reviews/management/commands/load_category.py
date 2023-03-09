from django.core.management import BaseCommand
from reviews.models import Category

from ._loader import data_loader


class Command(BaseCommand):
    def handle(self, *args, **options):
        data_loader(Category, 'category.csv')
