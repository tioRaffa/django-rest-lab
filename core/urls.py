
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('cursos.urls')),
    path('api/v1/', include('ToDoList.urls')),
    path('api/v1/', include('contatos.urls')),
    path('api/v1/', include('book.urls')),
    path('api/v1/', include('weather_app.urls')),
]
