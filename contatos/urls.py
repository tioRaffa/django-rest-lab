from django.urls import path
from contatos.views import ContatosAPIView, ContatoAPIView

urlpatterns = [
    path('contatos/', ContatosAPIView.as_view(), name='contatos'),
    path('contato/<int:pk>/', ContatoAPIView.as_view(), name='contato'),
]