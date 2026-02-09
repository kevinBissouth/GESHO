from django.urls import path

from . import views
from gestionConsultation.views import add_patient

urlpatterns = [
    path("", views.index, name="index"),
    path("patient/", views.patient, name="patient"),
    path("medecin/", views.medecin, name="medecin"),
    path("specialite/", views.specialite, name="specialite"),
    path("patient/add_patient/", views.add_patient, name="add_patient"),
    path("specialite/add_specialite/", views.add_specialite, name="add_specialite"),
    path("medecin/add_medecin/", views.add_medecin, name="add_medecin"),
    path("consultation/add_consultation/", views.add_consultation, name="add_consultation"),

    # path("consultation/", views.consultation, name="consultation"),
]    