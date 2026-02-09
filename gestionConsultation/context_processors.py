from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Patient, Medecin, Specialite, Consultation


def infos_globales(request):
    patient_total = Patient.objects.count()
    medecin_total = Medecin.objects.count()
    specialite_totale = Specialite.objects.count()
    consultation_totale = Consultation.objects.count() 

    return { 'patient_total': patient_total, 'medecin_total': medecin_total, 'specialite_totale': specialite_totale, 'consultation_totale': consultation_totale }
