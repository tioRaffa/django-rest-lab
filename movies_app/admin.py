from django.contrib import admin
from .models import (
    AuthorModel,
    DirectorModel,
    Gender,
    LanguagesModel,
    MoviesModels,
    ProductionCompaniesModel,
    VideoModel
)


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'known_for_department')
    search_fields = ('name', 'known_for_department')
    list_filter = ('known_for_department',)
    ordering = ('name',)
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('name', 'known_for_department', 'profile_path')
        }),
        ('IDs', {
            'fields': ('tmdb_id',)
        }),
    )
    readonly_fields = ('tmdb_id',)


@admin.register(DirectorModel)
class DirectorModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('name', 'profile_path')
        }),
        ('IDs', {
            'fields': ('tbmdb_id',)
        }),
    )
    readonly_fields = ('tbmdb_id',)


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('name', 'tmdb_id')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(LanguagesModel)
class LanguagesModelAdmin(admin.ModelAdmin):
    list_display = ('lenguage', 'iso_639_1')
    search_fields = ('lenguage', 'iso_639_1')
    ordering = ('lenguage',)


@admin.register(MoviesModels)
class MoviesModelsAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'vote_average', 'status')
    search_fields = ('title', 'directors__name')
    list_filter = ('release_date', 'status', 'genres')
    ordering = ('-release_date',)
    fieldsets = (
        ('Informações Principais', {
            'fields': ('title', 'overview', 'poster_path', 'release_date', 'status')
        }),
        ('Detalhes', {
            'fields': ('runtime', 'original_language', 'indicative_rating', 'budget', 'revenue', 'popularity')
        }),
        ('Votos', {
            'fields': ('vote_average', 'vote_count')
        }),
        ('Equipe e Elenco', {
            'fields': ('directors', 'cast')
        }),
        ('Outros', {
            'fields': ('genres', 'spoken_lenguages', 'production_companies', 'imdb_id')
        }),
    )
    filter_horizontal = ('genres', 'spoken_lenguages', 'cast', 'production_companies', 'directors')


@admin.register(ProductionCompaniesModel)
class ProductionCompaniesModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'origin_country')
    search_fields = ('name', 'origin_country')
    list_filter = ('origin_country',)
    ordering = ('name',)


@admin.register(VideoModel)
class VideoModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'site', 'type', 'filme')
    search_fields = ('name', 'filme__title')
    list_filter = ('site', 'type')
    ordering = ('name',)
