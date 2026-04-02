from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Traiteur
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import TraiteurForm
from django.contrib import messages

# Create your views here.
# creer liste_traiteurs qui recupere tous les objets du modèle (Traiteur.objects.all()) et creer ensuite liste.html qui affiche chaque traiteur sous forme de "Card"(Nom, Specialité) avec un bouton "Voir le profil"
from .models import Traiteur
def liste_traiteurs(request):
    # recuperer les objets de la base de données    
    traiteurs = Traiteur.objects.all()
    return render(request, 'liste.html', {'traiteurs': traiteurs})


def detail_traiteur(request, id):
    traiteur = get_object_or_404(Traiteur, id=id)
    if traiteur.image and not traiteur.image.storage.exists(traiteur.image.name):
        traiteur.image.delete()
    return render(request, 'detail_traiteur.html', {'traiteur': traiteur})


def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Connexion réussie.")
            return redirect('liste_traiteurs')
        messages.error(request, "Identifiants invalides. Réessayez.")
    else:
        form = AuthenticationForm()
    return render(request, 'connexion.html', {'form': form})

def deconnexion(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Déconnexion réussie.")
        return redirect('liste_traiteurs')
    return render(request, 'deconnexion.html')



@login_required
def ajouter_traiteur(request):
    if not request.user.is_staff:
        messages.error(request, "Accès réservé aux admins.")
        return render(request, 'ajouter_traiteur.html', {'form': None})
    if request.method == 'POST':
        form = TraiteurForm(request.POST, request.FILES)
        if form.is_valid():
            traiteur = form.save()
            return redirect('detail_traiteur', id=traiteur.id)
    else:
        form = TraiteurForm()
    return render(request, 'ajouter_traiteur.html', {'form': form})

def accueil(request):
    return render(request, 'accueil.html')