from django.core.management import BaseCommand
from reviews.models import Review

from ._loader import data_loader


class Command(BaseCommand):
    def handle(self, *args, **options):
        data_loader(Review, 'review.csv')
