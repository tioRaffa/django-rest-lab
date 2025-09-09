from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from movies_app.models import MoviesModels
from movies_app.serializers.movie_serializer import MoviesSerializer
from movies_app.api.get_details import get_movie_details_by_id



class MoviesAPIView(APIView):
    def get(self, request):
        movies = MoviesModels.objects.filter(is_active=True)
        serializer = MoviesSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        movie_id = request.data.get('tmdb_id')
        if not movie_id:
            return Response({
                'error': 'O ID do filme (tmdb_id) é obrigatiorio'
            }, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            api_data = get_movie_details_by_id(movie_id)
            genres = api_data.get('genres')
            credits = api_data.get('credits')
            
            directors = [
                {
                    'name': member.get('name'),
                    'profile_path': member.get('profile_path'),
                    'tmdb_id': member.get('id')
                    
                    
                } for member in credits.get('crew', []) if member.get('job') == 'Director'
            ]
            
            
            cast = [
                {
                    'name': actor.get('name'),
                    'known_for_department': actor.get('known_for_department'),
                    'profile_path': actor.get('profile_path'),
                    'tmdb_id': actor.get('id')
                    
                } for actor in credits.get('cast', [])[:5]
            ]
                
            
            release_dates = api_data.get('release_dates')
            results = release_dates.get('results')
            indicative_rating = []
            for country_release in results:
                if country_release.get('iso_3166_1') == 'BR':
                    certification  = country_release.get('release_dates')[0].get('certification')
                    data = {
                        'iso_3166_1': 'BR',
                        'certification': certification
                    }
                    indicative_rating.append(data)
                    break
                    
            
            # spoken_languages
            
            filtered_data = {
                'title': api_data.get('title'),
                'directors':directors,
                'overview': api_data.get('overview'),
                'genres': genres,
                'release_date': api_data.get('release_date'),
                'original_language': api_data.get('original_language'),
                'runtime': api_data.get('runtime'),
                'indicative_rating': indicative_rating,
                'vote_average': api_data.get('vote_average'),
                'vote_count': api_data.get('vote_count'),
                'poster_path': api_data.get('poster_path'),
                'status': api_data.get('status'),
                'budget': api_data.get('budget'),
                'revenue': api_data.get('revenue'),
                'popularity': api_data.get('popularity'),
                # 'spoken_languages': ...,
                'cast': cast,
                # 'production_companies': ...,
                'imdb_id': api_data.get('imdb_id')
                
            }
            
            
            
            return Response(results)
            
            
            
            
        except ValueError as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({
                'error': f'Ocorreu um erro inseperado na requisição {str(e)}'
            },status=status.HTTP_400_BAD_REQUEST)