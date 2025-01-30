from tkinter.font import names
from xml.sax import parse

from django.urls import path
from .views import *

app_name = 'limsApp'


urlpatterns = [
    path('', home, name='home'),
    path('login/', loginview, name='login'),
    path('author/', authorView, name='author'),
    path('author/<int:author_id>/delete/', deleteAuthor, name='delete_author'),
    path('author/<int:author_id>/edit/', editAuthor, name='edit_author'),
    #path('utilisateurConnection/', userPageConnec, name='utilisateurConnection'),
    #path('utilisateurInscription/', userPageInscrip, name='utilisateurInscription'),

]
