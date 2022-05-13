from django.urls import path
from . import views

urlpatterns = [
    path('bonjour/',views.bonjour),
    path('saisie/',views.saisie),
    path('traitement/',views.traitement),
    path('',views.home),
    path('home/',views.home),
    path('ajoutpaire/',views.ajoutpaire),
    path("affiche/<int:id>/",views.affiche),
    path("delete/<int:id>",views.delete),
    path("update/<int:id>",views.update),
    path("updatepaire/<int:id>",views.updatepaire),
]