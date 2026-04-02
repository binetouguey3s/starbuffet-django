# Star Buffet (Django)

## Objectif
Transformer le site statique en application web Django avec une architecture MVT (Model‑View‑Template) pour gérer l’annuaire des traiteurs et l’authentification.

## Étapes réalisées (A à Z)

**1) Création du projet et de l’application**
1. Création du projet Django `starbuffet_project`.
2. Création de l’application `services`.
3. Ajout de `services` dans `INSTALLED_APPS`.

**2) Modélisation**
1. Création du modèle `Traiteur` dans `services/models.py` avec :
   - `nomcomplet`, `specialites`, `description`, `adresse`, `email`, `telephone`
   - `est_actif` (Boolean)
   - `datedecreation` (auto_now_add)
   - `image` (ImageField)
2. Enregistrement du modèle dans `services/admin.py`.
3. Migrations :
   - `python manage.py makemigrations`
   - `python manage.py migrate`

**3) URLs et vues**
1. Création des routes dans `services/urls.py` :
   - Liste : `/liste/` 
   - Détail : `/traiteurs/<int:id>/`
   - Connexion : `/connexion/`
   - Déconnexion : `/deconnexion/`
   - Ajouter : `/traiteurs/ajouter/`
2. Vues correspondantes dans `services/views.py` :
   - `liste_traiteurs`
   - `detail_traiteur`
   - `connexion`
   - `deconnexion`
   - `ajouter_traiteur`

**4) Templates**
1. Base : `templates/base.html` (header/footer communs).
2. Liste : `services/templates/liste.html`.
3. Détail : `services/templates/detail_traiteur.html`.
4. Connexion / Déconnexion : `services/templates/connexion.html`, `services/templates/deconnexion.html`.
5. Ajout : `services/templates/ajouter_traiteur.html`.

**5) Authentification & Sécurité**
1. Authentification Django native.
2. Pages de connexion/déconnexion.
3. Accès à “Ajouter” réservé aux admins (`is_staff`).

**6) Formulaires**
1. Création d’un `ModelForm` dans `services/forms.py` pour ajouter un traiteur.
2. Page `/traiteurs/ajouter/` opérationnelle.

**7) Statics & Media**
1. Statics (CSS/images) dans `static/`.
2. Media (images uploadées) dans `media/traiteurs/`.
3. CSS organisés :
   - `static/css/common.css`
   - `static/css/traiteur.css`
   - `static/css/detail.css`
   - `static/css/forms.css`
   - `static/css/auth.css`

## Installation & Lancement
```bash
python -m venv venv
source venv/bin/activate
pip freeze >  requirement.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Accès Admin
- `/admin/` pour gérer les traiteurs
- Seuls les comptes **staff/admin** peuvent ajouter via `/traiteurs/ajouter/`

## Vérifications finales
1. Liste accessible (`/liste/`).
2. Détail accessible (`/traiteurs/<id>/`).
3. Connexion/déconnexion fonctionnelles.
4. Ajout traiteur bloqué pour non‑admin.
5. Images statiques et media visibles.
