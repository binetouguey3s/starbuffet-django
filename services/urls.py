from django.urls import path
from . import views 

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('liste-traiteurs/', views.liste_traiteurs, name='liste_traiteurs'),
    path('traiteurs/<int:id>/', views.detail_traiteur, name='detail_traiteur'),
    path('traiteurs/ajouter/', views.ajouter_traiteur, name='ajouter_traiteur'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
]
