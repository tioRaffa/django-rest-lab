from django.urls import path
from movies_app.views import SearchMovieByNameAdminAPIView, MovieListCreateView, MovieRetrieveUpdateView

urlpatterns = [
     path('movies/search/admin/', SearchMovieByNameAdminAPIView.as_view(), name='search_movie'),
     path('movies/',MovieListCreateView.as_view(), name='Movies'),
     path('movies/<int:pk>/', MovieRetrieveUpdateView.as_view(), name='Movie'),
 ]