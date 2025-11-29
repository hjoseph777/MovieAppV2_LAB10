from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie

class MovieModelTest(TestCase):
    def test_movie_creation(self):
        movie = Movie.objects.create(
            name="Test Movie",
            genre="Test Genre",
            description="Test Description"
        )
        self.assertEqual(movie.name, "Test Movie")
        self.assertEqual(str(movie), "Test Movie")
