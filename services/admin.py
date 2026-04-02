from django.contrib import admin
from .models import Traiteur
# Register your models here.

class TraiteurAdmin(admin.ModelAdmin):
    list_display = ('nomcomplet', 'specialites', 'email', 'est_actif')
    list_filter = ('est_actif', 'specialites')
    search_fields = ('nomcomplet', 'specialites')

admin.site.register(Traiteur, TraiteurAdmin)
