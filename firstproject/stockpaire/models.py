from django.db import models

# Create your models here.

class paire(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    nom = models.CharField(max_length=100) # défini un champs de type texte de 100 caractères maximum
    marque = models.CharField(max_length = 100)
    annee = models.DateField(blank=True, null = True) # champs de type date, pouvant être null ou ne pas être rempli# champs de type entier devant être obligatoirement rempli
    type = models.CharField(max_length=100, null = True, blank = True) # champs de type text long

    def __str__(self):
        chaine = f"{self.nom} faite par {self.marque} le {self.annee}."
        return chaine

    def dico(self):
        return {"nom" : self.nom, "marque" : self.marque, "annee":self.annee , "type" : self.type }

class couleurpaireiden(models.Model):  # défini un champs de type texte de 100 caractères maximum
    quantite = models.DateField(blank=True, null=True)  # champs de type date, pouvant être null ou ne pas être rempli
    modelepaire1 = models.ForeignKey(paire, on_delete=models.CASCADE, null="True")  # champs de type entier devant être obligatoirement rempli
    taille = models.CharField(max_length=100, null=True, blank=True)
    couleur = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        chaine = f"{self.nom} faite par {self.marque} le {self.annee}."
        return chaine

    def dico(self):
        return {"quantite" : self.quantite, "modelepaire1" : self.modelepaire1, "taille":self.taille , "couleur" : self.couleur }
