from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class paireform(ModelForm):
    class Meta:
        model = models.paire
        fields = ('nom', 'annee', 'marque','type')
        labels = {
            'nom' : _('Nom de la chaussure'),
            'annee' : _('Année de sortie') ,
            'marque' : _('Marque'),
            'type' : _('Type')
        }

class couleurpaireiden(ModelForm):
    class Meta:
        model = models.couleurpaireiden
        fields = ('quantite', 'modelepaire1', 'taille', 'couleur')
        labels = {
            'quantite' : _('Nombre de paire disponibles dans le monde') ,
            'modelepaire1' : _('Le modéle de la paire'),
            'taille' : _('La taille la plus répondue '),
            'couelur': _('Autre coloris : ')
        }

