from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from django.db.models import Q
from .models import Movie
from .forms import MovieForm, CustomUserCreationForm

# Basic CRUD operations for our movie app - pretty straightforward stuff

def home(request):
    # Just the landing page - nothing fancy here
    return render(request, 'movie/home.html')

def movie_list(request):
    # TODO: might want to add pagination later if we get too many movies
    movies = Movie.objects.all()
    return render(request, 'movie/movie_list.html', {'movies': movies})

def movie_detail(request, id):
    # Get the movie or show 404 if it dosn't exist
    movie = get_object_or_404(Movie, pk=id)
    return render(request, 'movie/movie_detail.html', {'movie': movie})

def movie_search(request):
    query = request.GET.get('q')
    movies = []  # start with empty list
    
    if query:
        # Search across name, genre, and description - covers most use cases
        movies = Movie.objects.filter(
            Q(name__icontains=query) | 
            Q(genre__icontains=query) | 
            Q(description__icontains=query)
        )
    return render(request, 'movie/movie_search.html', {'movies': movies, 'query': query})

@login_required
def movie_add(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            # console.log('form validation passed'); // left from debugging
            form.save()
            messages.success(request, 'Movie added successfully!')
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movie/movie_form.html', {'form': form, 'title': 'Add Movie'})

@login_required
def movie_edit(request, id):
    movie = get_object_or_404(Movie, pk=id)
    
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()  # Django handles the update automagically
            messages.success(request, 'Movie updated successfully!')
            return redirect('movie_detail', id=movie.id)
    else:
        # Pre-populate form with existing data
        form = MovieForm(instance=movie)
    return render(request, 'movie/movie_form.html', {'form': form, 'title': 'Edit Movie', 'movie': movie})

@login_required
def movie_delete(request, id):
    movie = get_object_or_404(Movie, pk=id)
    
    if request.method == 'POST':
        # Actually delete the movie - no going back after this!
        movie.delete()
        messages.success(request, 'Movie deleted successfully!')
        return redirect('movie_list')
    
    # Show confirmation page first (safety measure)
    return render(request, 'movie/movie_confirm_delete.html', {'movie': movie})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Auto-login after registration - better UX
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def custom_logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html')