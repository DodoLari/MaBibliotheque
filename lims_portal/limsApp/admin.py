from django.contrib import admin
from .models import Auteur, Client, Classification, Fournisseur, Livre, Ecrire, Emprunter, Acheter

# Enregistrer le modèle Auteur
class AuteurAdmin(admin.ModelAdmin):
    list_display = ('prenom_aut', 'nom_aut', 'adr_aut')
    search_fields = ('nom_aut', 'prenom_aut')
    list_filter = ('nom_aut',)

admin.site.register(Auteur, AuteurAdmin)

# Enregistrer le modèle Client (hérite de User)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('prenom_cl', 'nom_cl', 'num_tel_cl', 'adr_cl')
    search_fields = ('nom_cl', 'prenom_cl')
    list_filter = ('nom_cl',)

admin.site.register(Client, ClientAdmin)

# Enregistrer le modèle Classification
class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('type',)
    search_fields = ('type',)

admin.site.register(Classification, ClassificationAdmin)

# Enregistrer le modèle Fournisseur
class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('prenom_four', 'nom_four', 'num_tel', 'adr_four')
    search_fields = ('nom_four', 'prenom_four')
    list_filter = ('nom_four',)

admin.site.register(Fournisseur, FournisseurAdmin)

# Enregistrer le modèle Livre
class LivreAdmin(admin.ModelAdmin):
    list_display = ('ISBN', 'titre', 'edition', 'NbrDePages', 'classification')
    search_fields = ('titre', 'ISBN')
    list_filter = ('classification',)

admin.site.register(Livre, LivreAdmin)

# Enregistrer le modèle Ecrire
class EcrireAdmin(admin.ModelAdmin):
    list_display = ('livre', 'auteur')
    search_fields = ('livre__titre', 'auteur__prenom_aut', 'auteur__nom_aut')

admin.site.register(Ecrire, EcrireAdmin)

# Enregistrer le modèle Emprunter
class EmprunterAdmin(admin.ModelAdmin):
    list_display = ('livre', 'client')
    search_fields = ('livre__titre', 'client__prenom_cl', 'client__nom_cl')

admin.site.register(Emprunter, EmprunterAdmin)

# Enregistrer le modèle Acheter
class AcheterAdmin(admin.ModelAdmin):
    list_display = ('livre', 'fournisseur', 'date_achat', 'prix_achat', 'quantite_acheter')
    search_fields = ('livre__titre', 'fournisseur__nom_four')
    list_filter = ('date_achat',)

admin.site.register(Acheter, AcheterAdmin)
