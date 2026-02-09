from django.forms import widgets
from django import forms
from .models import *

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['num_patient' , 'nom_patient']
        widgets = {
            
            'nom_patient' : forms.TextInput(attrs= {
                'placeholder' : 'exemple : John',
                'class' : 'p-[5px] rounded-lg text-white bg-indigo-700 font-semibold',
            }),
        }


class MedecinForm(forms.ModelForm):
    # Specialite_medecin = forms.ModelChoiceField(queryset=Specialite.objects.all())
    class Meta:
        model = Medecin
        empty_label = "choisir une specialite"
        fields = ['code_medecin', 'nom_medecin', 'specialite_medecin']
        widgets = {
            'code_medecin' : forms.TextInput(attrs= {
                'placeholder' : 'exemple : MEDKR1',
                'class' : 'p-[5px] rounded-lg text-white bg-indigo-700 w-full font-semibold',
            }),

            'nom_medecin' : forms.TextInput(attrs= {
                'placeholder' : 'exemple : John',
                'class' : 'p-[5px] rounded-lg text-white bg-indigo-700 w-full font-semibold',

            }),

            'specialite_medecin' : forms.Select(attrs= {
                'class' : 'w-full p-[5px] border rounded-lg bg-indigo-700 text-white',
                
                
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['specialite_medecin'].empty_label = "Choisir une Specialite"


class SpecialiteForm(forms.ModelForm):
    class Meta:
        model = Specialite
        fields = ['code_specialite', 'nom_specialite']
        widgets = {
            'code_specialite': forms.TextInput(attrs= {
                'placeholder': 'exemple: CH',
                'class' : 'p-[5px] rounded-lg text-white bg-indigo-700 w-full font-semibold',

            }),

            'nom_specialite' : forms.TextInput(attrs= {
                'placeholder' : 'exemple : Chirugie',
                'class' : 'p-[5px] rounded-lg text-white bg-indigo-700 w-full font-semibold',

            }),
        } 


class ConsultationForm(forms.ModelForm):
    # date = forms.DateTimeField(input_formats=['%d/%m/%y %H:%M:%S'])
    class Meta:
        model = Consultation
        fields = ['id_consultation', 'compteur', 'consult_num_patient', 'consult_code_medecin', 'motif', 'diagnostic', 'prescription', 'date', 'date_medecin', 'date_patient']
        widgets = {
            'consult_num_patient' : forms.Select(attrs= {
                'class' : 'p-[5px] rounded-lg text-white bg-indigo-700 w-[340px] font-semibold',

            }),

            'consult_code_medecin' : forms.Select(attrs= {
                'placeholder' : 'exemple : Anderson--(MEDJ3)',
                'class' : 'p-[5px] rounded-lg text-white bg-indigo-700 w-[340px] font-semibold',

            }),

            'motif' : forms.TextInput(attrs= {
                'placeholder' : 'exemple : mal de tete',
                'class' : 'p-[5px] rounded-lg text-white bg-indigo-700 w-full font-semibold',
            }),

            'diagnostic': forms.Textarea(attrs= {
                'placeholder': 'exemple: Aucune maladie detectee',
                'class' : 'p-[5px] rounded-lg text-white bg-indigo-700 w-[340px] font-semibold resize-none',
            }),

            'prescription' : forms.Textarea(attrs= {
                'placeholder' : 'exempl: paracetamol',
                'class' : 'p-[5px] rounded-lg text-white bg-indigo-700 w-[340px] font-semibold resize-none',

            }),

            'date' : forms.DateTimeInput(format='%d/%m/%y %H:%M', attrs= {
                'type': 'datetime-local',
                'class' : 'p-[5px] rounded-lg text-white bg-indigo-700 w-full font-semibold',
                
            }),

            
        }   
    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.fields['consult_num_patient'].empty_label = "Choisir un Patient"
         self.fields['consult_code_medecin'].empty_label = "Choisir un Medecin"
            