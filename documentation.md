# Documentation complète (pas à pas) — Projet Star Buffet (Django)

Ce document explique **toutes les étapes** réalisées, avec des détails adaptés à un débutant. L’objectif est que tu comprennes **pourquoi** chaque action est faite et **comment** elle fonctionne.

---

## 1) Objectif du projet

Tu avais un **site statique** (HTML/CSS). Le but est de le transformer en **application web dynamique** avec Django en utilisant l’architecture **MVT** :

- **M (Model)** : les données (ex: Traiteur)
- **V (View)** : la logique Python qui prépare les données
- **T (Template)** : les pages HTML qui affichent les données

---

## 2) Création du projet Django et de l’application

### 2.1 Créer le projet
Un projet Django contient les réglages globaux (settings, urls, etc.).

### 2.2 Créer l’application `services`
Une application regroupe une fonctionnalité précise : ici, **gestion des traiteurs**.

Dans `settings.py`, on ajoute :

```
INSTALLED_APPS = [
    ...
    "services",
]
```

Pourquoi ? Django doit connaître l’application pour charger ses modèles, templates, urls, etc.

---

## 3) Modèle de données (Model)

Le modèle `Traiteur` représente un traiteur dans la base de données.

**Champs principaux :**
- `nomcomplet` : nom complet
- `specialites` : spécialités culinaires
- `description` : description
- `adresse` : adresse
- `email` : email
- `telephone` : téléphone
- `est_actif` : actif / vérifié
- `datedecreation` : date automatique de création
- `image` : image uploadée

Exemple (simplifié) :

```python
class Traiteur(models.Model):
    nomcomplet = models.CharField(max_length=100)
    specialites = models.CharField(max_length=200)
    description = models.TextField()
    adresse = models.CharField(max_length=200)
    est_actif = models.BooleanField(default=True)
    email = models.EmailField()
    datedecreation = models.DateTimeField(auto_now_add=True)
    telephone = models.CharField(max_length=20)
    image = models.ImageField(upload_to="traiteurs/", null=True, blank=True)
```

### Pourquoi faire des migrations ?
Django ne modifie pas directement la base. On doit **générer** puis **appliquer** des migrations :

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 4) Administration Django

Pour gérer facilement des traiteurs (ajout, suppression, modification), on active le modèle dans l’admin :

```python
# services/admin.py
from django.contrib import admin
from .models import Traiteur

class TraiteurAdmin(admin.ModelAdmin):
    list_display = ("nomcomplet", "specialites", "email", "est_actif")
    list_filter = ("est_actif", "specialites")
    search_fields = ("nomcomplet", "specialites")

admin.site.register(Traiteur, TraiteurAdmin)
```

Puis on crée un superutilisateur :

```bash
python manage.py createsuperuser
```

---

## 5) URLs et Vues

### 5.1 URLs du projet
Dans `starbuffet_project/urls.py`, on inclut les URLs de l’app :

```python
path("", include("services.urls"))
```

### 5.2 URLs de l’app
Dans `services/urls.py`, on définit les routes :

- `/liste/` → liste des traiteurs
- `/traiteurs/<id>/` → détail traiteur
- `/connexion/` → login
- `/deconnexion/` → logout
- `/traiteurs/ajouter/` → formulaire d’ajout

### 5.3 Vues
Chaque route appelle une fonction Python qui renvoie un HTML :

**Liste :**
```python
traiteurs = Traiteur.objects.all()
return render(request, "liste.html", {"traiteurs": traiteurs})
```

**Détail :**
```python
traiteur = get_object_or_404(Traiteur, id=id)
return render(request, "detail_traiteur.html", {"traiteur": traiteur})
```

---

## 6) Templates (HTML dynamiques)

### 6.1 Base HTML (`templates/base.html`)
Contient le header + footer partagés.
Les pages héritent avec :

```django
{% extends "base.html" %}
```

### 6.2 Liste (`liste.html`)
Affiche chaque traiteur en “card” :

```django
{% for traiteur in traiteurs %}
   {{ traiteur.nomcomplet }}
{% endfor %}
```

### 6.3 Détail (`detail_traiteur.html`)
Affiche les infos d’un seul traiteur.
Image de fond dynamique :

```django
{% if traiteur.image %}
   url("{{ traiteur.image.url }}")
{% else %}
   url("{% static \"images/default.jpg\" %}")
{% endif %}
```

---

## 7) Authentification (Login/Logout)

### Connexion
- Utilise `AuthenticationForm` de Django.
- Si OK → `login(request, user)`

### Déconnexion
- Sur POST → `logout(request)`

### Sécurité
- La page **ajouter** est réservée aux admins (`is_staff`).
- Si un non‑admin tente, un message s’affiche :
  “Accès réservé aux admins.”

---

## 8) Formulaire d’ajout (ModelForm)

Un `ModelForm` permet de générer automatiquement le formulaire depuis le modèle :

```python
class TraiteurForm(forms.ModelForm):
    class Meta:
        model = Traiteur
        fields = [...]
```

La vue `ajouter_traiteur` enregistre un nouveau traiteur avec `form.save()`.

---

## 9) Statics et Media

### Statics
- CSS/JS/Images fixes → `static/`
- Chargement dans les templates :

```django
{% load static %}
<link rel="stylesheet" href="{% static \"css/traiteur.css\" %}">
```

### Media
- Images uploadées → `media/traiteurs/`
- Django sert ces fichiers en dev avec :

```python
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 10) CSS (organisation)

- `common.css` : header/footer commun
- `traiteur.css` : page liste
- `detail.css` : page détail
- `forms.css` + `auth.css` : pages formulaires

---

## 11) Menu burger

Un script JS gère l’ouverture du menu :

- `static/js/nav.js`
- Il active la classe `.active` sur `.nav` et `.button`.

---

## 12) Débogage courant

### Erreur “no such column”
→ Migration oubliée. Refaire :

```bash
python manage.py makemigrations
python manage.py migrate
```

### CSS non chargé
→ Vérifier le chemin `/static/...`

---

## 13) Récapitulatif final

✅ Liste dynamique
✅ Détail dynamique
✅ Authentification
✅ Ajout sécurisé
✅ Admin OK
✅ CSS organisé
✅ Statics & Media

---

Si tu veux, je peux compléter ce document avec des captures d’écran ou un schéma MVT simplifié.

---

## Schéma MVT (simplifié)

```
Utilisateur (navigateur)
        |
        v
URL -> urls.py ------------------------------+
        |                                   |
        v                                   |
views.py (logique)                           |
        |                                   |
        +----> Model (models.py)            |
        |          |                        |
        |          v                        |
        |     Base de données               |
        |                                   |
        v                                   |
Template (HTML) <--------- contexte --------+
        |
        v
Réponse HTML au navigateur
```

**Lecture rapide :**
1. L’utilisateur demande une URL.
2. `urls.py` envoie la requête vers la bonne vue.
3. La vue prépare les données via le modèle.
4. Le template reçoit les données et génère le HTML.
5. Le HTML revient au navigateur.
