from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = 'Populate the database with sample movie data'

    def handle(self, *args, **options):
        # Clear existing movies first
        Movie.objects.all().delete()
        
        # Movie data - feel free to add more later
        movies_data = [
            {
                'name': 'The Shawshank Redemption',
                'genre': 'Drama',
                'description': 'A man wrongfully imprisoned finds hope and redemption through the common decency of the men serving time with him.'
            },
            {
                'name': 'The Godfather',
                'genre': 'Crime',
                'description': 'The aging patriarch of an organized crime dynasty transfers control to his reluctant son.'
            },
            {
                'name': 'Inception',
                'genre': 'Sci-Fi',
                'description': 'A thief who steals secrets from dreams is given the final job of planting an idea deep within a target\'s subconscious.'
            },
            {
                'name': 'The Dark Knight',
                'genre': 'Action',
                'description': 'Batman faces his greatest challenge yet as the Joker wreaks havoc and chaos on Gotham City.'
            },
            {
                'name': 'Forrest Gump',
                'genre': 'Drama',
                'description': 'A man with a low IQ accomplishes great things in his life and influences the lives of those around him.'
            },
            {
                'name': 'Pulp Fiction',
                'genre': 'Crime',
                'description': 'The lives of two mob hitmen, a boxer, a gangster and his wife intertwine in four tales of violence and redemption.'
            },
            {
                'name': 'The Matrix',
                'genre': 'Sci-Fi',
                'description': 'A computer programmer discovers reality is a simulation and joins a rebellion to free humanity from their digital prison.'
            },
            {
                'name': 'Goodfellas',
                'genre': 'Crime',
                'description': 'The story of Henry Hill and his life in the mob, covering his relationship with his wife and his mob partners.'
            },
            {
                'name': 'The Lord of the Rings: The Return of the King',
                'genre': 'Fantasy',
                'description': 'The final battle for Middle-earth begins as Frodo and Sam approach Mount Doom to destroy the One Ring.'
            },
            {
                'name': 'Fight Club',
                'genre': 'Thriller',
                'description': 'An insomniac office worker forms an underground fight club that evolves into an anarchist organization.'
            }
        ]
        
        # Create movies from our data list
        for movie_data in movies_data:
            Movie.objects.create(**movie_data)
            # print(f'Added: {movie_data["name"]}')  # debugging
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created movie: {movie_data["name"]}')
            )
        
        total_count = Movie.objects.count()  # double check our work
        self.stdout.write(
            self.style.SUCCESS(f'Successfully populated database with {total_count} movies!')
        )