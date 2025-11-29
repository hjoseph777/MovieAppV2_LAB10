from django.contrib import admin
from .models import Movie

# Basic admin config for movies - pretty standard stuff
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'genre', 'updated']  # what shows in the list view
    list_filter = ['genre', 'updated']  # sidebar filters
    search_fields = ['name', 'genre']  # search functionality
    
    # Note: could add more fields like ordering or readonly_fields later
