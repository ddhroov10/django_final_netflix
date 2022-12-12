from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

AGE_CHOICES = (
    ('All', 'All'),
    ('Kids', 'Kids'),
)

# Note - Right part of the pair is the text for the front end display
# Note2 - Right part of the pair is the text through which we will refer the object in the backend.

MOVIE_CHOICES = (
    ('seasonal', 'Seasonal'),
    ('single', 'Single'),
)

# One customer can have multiple profiles like 'for brother', 'for parents', etc.
class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile', blank=True)

# Class for each profile
class Profile(models.Model):
    name = models.CharField(max_length=1000)
    age_limit = models.CharField(choices=AGE_CHOICES, max_length=10)

    #id for each user to different their profiles.
    uuid = models.UUIDField(default=uuid.uuid4) 

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)

    # automatically create date and time for the movie created
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(choices=MOVIE_CHOICES, max_length=10)
    video = models.ManyToManyField('Video')

    # Movie thumbnail
    image = models.ImageField(upload_to='covers')
    age_limit = models.CharField(choices=AGE_CHOICES, max_length=10)

    def __str__(self):
        return self.title

class MovieBollywood(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)

    # automatically create date and time for the movie created
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(choices=MOVIE_CHOICES, max_length=10)
    video = models.ManyToManyField('Video')

    # Movie thumbnail
    image = models.ImageField(upload_to='covers')
    age_limit = models.CharField(choices=AGE_CHOICES, max_length=10)

    def __str__(self):
        return self.title

class MovieComedy(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)

    # automatically create date and time for the movie created
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(choices=MOVIE_CHOICES, max_length=10)
    video = models.ManyToManyField('Video')

    # Movie thumbnail
    image = models.ImageField(upload_to='covers')
    age_limit = models.CharField(choices=AGE_CHOICES, max_length=10)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=1000)
    file = models.FileField(upload_to='movies')

    def __str__(self):
        return self.title
