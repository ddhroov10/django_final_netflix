from django.urls import path
from .views import Home

app_name = 'netflixapp'

urlpatterns = [
    path('', Home.as_view(), name="home")
]