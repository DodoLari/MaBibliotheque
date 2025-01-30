from django import forms
from .models import Auteur

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class AuthorCreationForm(forms.ModelForm):  # Changement de Form à ModelForm
    class Meta:
        model = Auteur
        fields = ['nom_aut', 'prenom_aut', 'adr_aut']  # Liste des champs du modèle Auteur

        widgets = {
            'nom_aut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'auteur'}),
            'prenom_aut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom de l\'auteur'}),
            'adr_aut': forms.TextInput(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Adresse de l\'auteur'}),
        }
