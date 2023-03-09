from django.core.management import BaseCommand
from reviews.models import Genre, Title

from ._loader import add_genres, data_loader


class Command(BaseCommand):
    def handle(self, *args, **options):
        data_loader(Title, 'titles.csv')
        add_genres(Title, Genre, 'genre_title.csv')
