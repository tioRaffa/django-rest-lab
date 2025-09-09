from rest_framework import serializers
from movies_app.models.movie_model import MoviesModels

from .author_serializer import AuthorSerializer
from .director_serializer import DirectorSerializer
from .genres_serializer import GenderSerializer
from .language_serializer import LanguageSerializer
from .production_comp_serializer import ProductionCompaniesSerializer

class MoviesSerializer(serializers.ModelSerializer):
    cast = AuthorSerializer(many=True)
    directors = DirectorSerializer(many=True)
    genres = GenderSerializer(many=True)
    spoken_languages = LanguageSerializer(many=True)
    productions_companies = ProductionCompaniesSerializer(many=True)
    
    class Meta:
        model = MoviesModels
        fields = [
            'id',
            'title',
            'overview',
            'poster_path',
            'release_date',
            'directors',
            'genres',
            'original_language',
            'run_time',
            'indicative_rating',
            'vote_varage',
            'vote_count',
            'status',
            'budget',
            'revenue',
            'popularity',
            'spoken_languages',
            'cast',
            'productions_companies',
            'video',
            'imdb_id',
            'is_active'
        ]
        extra_kwargs = {
            'imdb_id': {'write_only': True},
            'is_active': {'write_only': True}
        }

