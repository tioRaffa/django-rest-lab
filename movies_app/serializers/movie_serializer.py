from rest_framework import serializers
from movies_app.models.movie_model import MoviesModels


class MoviesSerializer(serializers.ModelSerializer):
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
        ]
        extra_kwargs = {
            'imdb_id': {'write_only': True}
        }

