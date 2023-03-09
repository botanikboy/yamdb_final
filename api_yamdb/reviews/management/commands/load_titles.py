from django.core.management import BaseCommand

from ._loader import data_loader, add_genres
from reviews.models import Title, Genre


class Command(BaseCommand):
    def handle(self, *args, **options):
        data_loader(Title, 'titles.csv')
        add_genres(Title, Genre, 'genre_title.csv')
