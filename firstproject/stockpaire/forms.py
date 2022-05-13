from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class paireform(ModelForm):
    class Meta:
        model = models.paire
        fields = ('nom', 'annee', 'marque', 'couleur','type')
        labels = {
            'nom' : _('Nom de la chaussure'),
            'annee' : _('Année de sortie') ,
            'marque' : _('Marque'),
            'couleur' : _('Couleur dominante'),
            'type' : _('Type')
        }

