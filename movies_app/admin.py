from django.contrib import admin
from .models.author_model import AuthorModel
from .models.director_model import DirectorModel
from .models.language_model import LanguagesModel
from .models.movie_model import MoviesModels, Gender
from .models.production_companies_model import ProductionCompaniesModel
from .models.video_model import VideoModel

@admin.register(MoviesModels)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'indicative_rating', 'status', 'vote_average', 'is_active')
    

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('name', 'tmdb_id')

@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'known_for_department', 'tmdb_id')

@admin.register(DirectorModel)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'tmdb_id')

@admin.register(LanguagesModel)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('language', 'iso_639_1')

@admin.register(ProductionCompaniesModel)
class ProductionCompaniesAdmin(admin.ModelAdmin):
    list_display = ('name', 'origin_country', 'tmdb_id')

@admin.register(VideoModel)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'site', 'filme')
