from django.db import models
from django.contrib.auth.models import User


class Auteur(models.Model):
    nom_aut = models.CharField(max_length=50)
    prenom_aut = models.CharField(max_length=50)
    adr_aut = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.prenom_aut} {self.nom_aut}"


class Client(User):
    nom_cl = models.CharField(max_length=50)
    prenom_cl = models.CharField(max_length=50)
    num_tel_cl = models.CharField(max_length=50)
    adr_cl = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.prenom_cl} {self.nom_cl}"

    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)


class Classification(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class Fournisseur(models.Model):
    nom_four = models.CharField(max_length=50)
    prenom_four = models.CharField(max_length=50)
    num_tel = models.CharField(max_length=50)
    adr_four = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.prenom_four} {self.nom_four}"


class Livre(models.Model):
    ISBN = models.CharField(max_length=25, primary_key=True)
    titre = models.CharField(max_length=50)
    edition = models.CharField(max_length=50)
    NbrDePages = models.IntegerField(null=True, blank=True)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre


class Ecrire(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("livre", "auteur")


class Emprunter(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("livre", "client")


class Acheter(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    date_achat = models.DateField()
    prix_achat = models.IntegerField()
    quantite_acheter = models.IntegerField(blank=True, null=True)

    class Meta:
        unique_together = ("livre", "fournisseur")
