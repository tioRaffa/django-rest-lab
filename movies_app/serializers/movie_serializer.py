from rest_framework import serializers
from movies_app.models.movie_model import MoviesModels, Gender
from movies_app.models.author_model import AuthorModel
from movies_app.models.director_model import DirectorModel
from movies_app.models.language_model import LanguagesModel
from movies_app.models.production_companies_model import ProductionCompaniesModel

from .author_serializer import AuthorSerializer
from .director_serializer import DirectorSerializer
from .genres_serializer import GenderSerializer
from .language_serializer import LanguageSerializer
from .production_comp_serializer import ProductionCompaniesSerializer

class MoviesSerializer(serializers.ModelSerializer):
    cast = AuthorSerializer(many=True)
    authors_ids = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=AuthorModel.objects.all(),
        source='cast',
        many=True,
        required=False,
        help_text='Id de atores'
    )
    
    directors = DirectorSerializer(many=True)
    directors_ids = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=DirectorModel.objects.all(),
        source='directors',
        many=True,
        required=False,
        help_text='Id de diretores'
    )
    
    genres = GenderSerializer(many=True)
    genres_ids = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Gender.objects.all(),
        source='genres',
        many=True,
        required=False,
        help_text='ID de generos'
    )
    
    spoken_languages = LanguageSerializer(many=True)
    languages_ids = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=LanguagesModel.objects.all(),
        source='spoken_languages',
        many=True,
        required=False,
        help_text='ID de linguagens'
    )
    
    production_companies = ProductionCompaniesSerializer(many=True)
    companies_ids = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=ProductionCompaniesModel.objects.all(),
        source='production_companies',
        many=True,
        required=False,
        help_text='ID de companies'
    )
    
    class Meta:
        model = MoviesModels
        fields = [
            'id',
            'title',
            'overview',
            'poster_path',
            'release_date',
            'directors',
            'directors_ids',
            'genres',
            'genres_ids',
            'original_language',
            'runtime',
            'indicative_rating',
            'vote_average',
            'vote_count',
            'status',
            'budget',
            'revenue',
            'popularity',
            'spoken_languages',
            'languages_ids',
            'cast',
            'authors_ids',
            'production_companies',
            'companies_ids',
            'tmdb_id',
            'is_active',
        ]
        extra_kwargs = {
            'tmdb_id': {'write_only': True},
            'is_active': {'write_only': True}
        }
        
    def create(self, validated_data):
        cast_data = validated_data.pop('cast', [])
        directors_data = validated_data.pop('directors', [])
        genres_data = validated_data.pop('genres', [])
        languages_data = validated_data.pop('spoken_languages', [])
        production_companies_data = validated_data.pop('production_companies', [])
        
        movie: MoviesModels = MoviesModels.objects.create(**validated_data)
        
        try:
            movie.full_clean()
        except ValueError as e:
            raise serializers.ValidationError(e)
        
        if cast_data:
            for actor_data in cast_data:
                actor, created = AuthorModel.objects.get_or_create(
                    tmdb_id=actor_data.get('tmdb_id'),
                    defaults=actor_data
                )
                movie.cast.add(actor)
                
        if directors_data:
            for director_data in directors_data:
                director, created = DirectorModel.objects.get_or_create(
                    tmdb_id=director_data.get('tmdb_id'),
                    defaults=director_data
                )
                movie.directors.add(director)
                
        if genres_data:
            for genre_data in genres_data:
                genre,created = Gender.objects.get_or_create(
                    tmdb_id=genre_data.get('tmdb_id'),
                    defaults=genre_data
                )
                movie.genres.add(genre)
                
        if languages_data:
            for language_data in languages_data:
                language, created = LanguagesModel.objects.get_or_create(
                    iso_639_1=language_data.get('iso_639_1'),
                    defaults=language_data
                )
                movie.spoken_languages.add(language)
                
        if production_companies_data:
            for production_companie in production_companies_data:
                companie, created = ProductionCompaniesModel.objects.get_or_create(
                    tmdb_id=production_companie.get('tmdb_id'),
                    defaults=production_companie
                )
                movie.production_companies.add(companie)
                
        return movie
