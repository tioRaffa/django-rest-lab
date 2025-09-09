from django.urls import path
from movies_app.views import SearchMovieByNameAdminAPIView, MoviesAPIView

urlpatterns = [
     path('movies/search/admin/', SearchMovieByNameAdminAPIView.as_view(), name='search_movie'),
     path('movies/',MoviesAPIView.as_view(), name='Movies')
 ]