from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template.context_processors import request
from .models import Patient, Medecin, Specialite, Consultation
from .forms import *


def add_patient(request):
    form = PatientForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('patient')
    return render(request, 'add_patient.html', {'form': form})

def add_specialite(request):
    form = SpecialiteForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('specialite')
    return render(request, 'add_specialite.html', {'form': form})

def add_medecin(request):
    form = MedecinForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('medecin')
    return render(request, 'add_medecin.html', {'form': form})

def add_consultation(request):
    form = ConsultationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'add_consultation.html', {'form': form})

def index(request):
    if request.method == 'POST' :
        if 'DELETE' in request.POST :
            pk = request.POST.get('pk')
            object = get_object_or_404(Consultation, pk = pk)
            object.delete()
            return redirect('index')
        
        elif 'UPDATE' in request.POST:
            pk = request.POST.get('pk')
            object = get_object_or_404(Consultation, pk=pk)
            form = PatientForm(request.POST, instance=object)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = ConsultationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')

    else:
        form = ConsultationForm()
    liste_consultations = Consultation.objects.all()
    return render(request, 'home.html', {'liste_consultations': liste_consultations, 'form': form})



def patient(request):
    if request.method == 'POST' :
        if 'DELETE' in request.POST :
            pk = request.POST.get('pk')
            object = get_object_or_404(Patient, pk = pk)
            object.delete()
            return redirect('patient')
        
        elif 'UPDATE' in request.POST:
            pk = request.POST.get('pk')
            object = get_object_or_404(Patient, pk=pk)
            form = PatientForm(request.POST, instance=object)
            if form.is_valid():
                form.save()
                return redirect('patient')
                
        else:
            form = PatientForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('patient')
            
    else:
        form = PatientForm()
        
    patients = Patient.objects.all()
    return render(request, 'patient.html', {'patients': patients, 'form': form})



def medecin(request):
    if request.method == 'POST' :
        if 'DELETE' in request.POST :
            pk = request.POST.get('pk')
            object = get_object_or_404(Medecin, pk = pk)
            object.delete()
            return redirect('medecin')
        
        elif 'UPDATE' in request.POST:
            pk = request.POST.get('pk')
            object = get_object_or_404(Medecin, pk=pk)
            form = PatientForm(request.POST, instance=object)
            if form.is_valid():
                form.save()
                return redirect('medecin')
            
        else:
            form = MedecinForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('medecin')
    else:
        form = MedecinForm()
    medecins = Medecin.objects.all()
    return render(request, 'medecin.html', {'medecins': medecins, 'form': form})



def specialite(request):
    if request.method == 'POST' :
        if 'DELETE' in request.POST :
            pk = request.POST.get('pk')
            object = get_object_or_404(Specialite, pk = pk)
            object.delete()
            return redirect('specialite')
        
        elif 'UPDATE' in request.POST:
            pk = request.POST.get('pk')
            object = get_object_or_404(Specialite, pk=pk)
            form = PatientForm(request.POST, instance=object)
            if form.is_valid():
                form.save()
                return redirect('specialite')
        else:
            form = SpecialiteForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('specialite')
    else:
        form = SpecialiteForm()
    specialites = Specialite.objects.all()
    return render(request, 'specialite.html', {'specialites': specialites, 'form': form})
