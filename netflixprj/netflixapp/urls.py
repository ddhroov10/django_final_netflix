from django.urls import path
from .views import Home, ProfileList, ProfileCreate, MovieList, MovieDetail, PlayMovie

app_name = 'netflixapp'

# all these url patterns goes to the views.py file and calls the class with the name mentioned with .as_view
urlpatterns = [
    path('', Home.as_view(), name="Home"),
    path('profiles/', ProfileList.as_view(), name="profile-list"),
    path('profiles/create/', ProfileCreate.as_view(), name="profile-create"),
    path('watch/<str:profile_id>/', MovieList.as_view(), name="movie-list"),
    path('watch/detail/<str:movie_id>/<str:movie_type>', MovieDetail.as_view(), name="movie-detail"),
    path('watch/play/<str:movie_id>/', PlayMovie.as_view(), name="play-movie") 
]