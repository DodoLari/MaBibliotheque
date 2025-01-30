from django.contrib.auth import authenticate, login, get_user, get_user_model
from django.shortcuts import (render)
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.template.context_processors import request
from .models import Client
from .models import Auteur
from django.db.models import Count
from .forms import AuthorCreationForm
from django.contrib import messages


# Create your views here.

def home(request):

    return render(request, "limsApp/home.html")


def loginview(request):

    return render(request, "limsApp/login.html")

def deleteAuthor(request, author_id):
    auteur = get_object_or_404(Auteur, id=author_id)

    if request.method == 'POST':
        auteur.delete()
        messages.success(request, "L'auteur a été supprimé avec succès.")
        return redirect('limsApp:author')  # Redirige vers la page des auteurs après la suppression

    # Si ce n'est pas un POST, on renvoie une erreur ou on redirige ailleurs
    return redirect('limsApp:author')


def editAuthor(request, author_id):
    auteur = get_object_or_404(Auteur, id=author_id)

    if request.method == 'POST':
        form = AuthorCreationForm(request.POST, instance=auteur)
        if form.is_valid():
            form.save()
            return redirect('limsApp:author')  # Redirige après modification avec succès

    return redirect('limsApp:author')

def authorView(request):
    if request.method == 'POST':
        form = AuthorCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('limsApp:author')
    else:
        form = AuthorCreationForm()

    auteurs = Auteur.objects.annotate(nombre_de_livres=Count('ecrire')).all()

    return render(request, "limsApp/auteur.html", {'auteurs': auteurs, 'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Associe l'utilisateur à la session
            return redirect('home')  # Redirige vers la page d'accueil
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


#def userPage(request):
#    return render(request, "limsApp/utilisateurPage.html")

#def userPageInscrip(request):
#   if request.method == 'POST':
#      nom = request.POST['nom']
#     prenom = request.POST['prenom']
#        adresse = request.POST['adresse']
#       numero_telephone = request.POST['Numero_tel']
#        username=request.POST['username']
#        password=request.POST['password']
#        print(nom, prenom, adresse, numero_telephone)
#        user = Client.objects.create_user(nom_cl=nom, prenom_cl=prenom, adr_cl=adresse, num_tel_cl=numero_telephone, username=username, password=password)
#        if user is not None:
#            return redirect('limsApp:utilisateurConnection')
#    return render(request, 'limsApp/utilisateurInscription.html')

#def userPageConnec(request):
#    if request.method == 'POST':
#        username=request.POST['username']
#        password=request.POST['password']
#        user = authenticate(request, username=username, password=password)
#        if user:
#            login(request, user)
#            if user.is_superuser:
#                redirect('lims:Admin')
#            else:
#                redirect('limsApp:utilisateurPage')
#    return render(request, "limsApp/utilisateurConnection.html")
