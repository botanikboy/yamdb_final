from django.core.management import BaseCommand
from reviews.models import Comment

from ._loader import data_loader


class Command(BaseCommand):
    def handle(self, *args, **options):
        data_loader(Comment, 'comments.csv')
