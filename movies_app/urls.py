from django.urls import path
from movies_app.views import SearchMovieByNameAdminAPIView

urlpatterns = [
     path('movies/search/admin/', SearchMovieByNameAdminAPIView.as_view(), name='search_movie'),
 ]