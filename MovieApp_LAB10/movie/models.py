from django.db import models

# Simple movie model - kept it basic for this demo
class Movie(models.Model):
    name = models.CharField(max_length=200)  # movie title
    genre = models.CharField(max_length=200)  # could use choices later
    description = models.TextField(null=True, blank=True)  # optional field
    updated = models.DateTimeField(auto_now=True)  # tracks last modification

    def __str__(self):
        # Return movie name for admin display
        return self.name
    
    # Note: might add rating field in future update