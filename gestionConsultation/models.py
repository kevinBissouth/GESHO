from django.db import models, IntegrityError
from django.utils.text import slugify
# Create your models here.

class Patient(models.Model):
    num_patient = models.AutoField(primary_key=True, unique=True , blank=False)
    nom_patient = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return f"{self.nom_patient}({self.num_patient})"


class Specialite(models.Model):
    code_specialite = models.CharField(max_length=9, primary_key=True, unique=True, blank=False)
    nom_specialite = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return f"{self.nom_specialite}--({self.code_specialite})"    


class Medecin(models.Model):
    code_medecin = models.CharField(max_length=9,primary_key=True, unique=True, blank=False)
    nom_medecin = models.CharField(max_length=20, blank=False)
    specialite_medecin = models.ForeignKey(Specialite, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return f"{self.nom_medecin}--({self.code_medecin})"


class Consultation(models.Model):
    id_consultation = models.CharField(primary_key=True, unique=True, blank=True, max_length=50)
    compteur = models.IntegerField(blank= True, unique=True, default=0)
    consult_num_patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)
    consult_code_medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE, blank=False)
    motif = models.CharField(max_length=50, blank=False)
    diagnostic = models.CharField(max_length=100, blank=False)
    prescription = models.CharField(max_length=100, blank=False)
    date = models.DateTimeField()
    date_medecin = models.SlugField(unique=True, blank= True)
    date_patient = models.SlugField(unique=True, blank= True)

    def save(self, *args, **kwargs):
        self.compteur = self.compteur + 1
        self.id_consultation = slugify(f"CONSULT-{self.compteur}")
        self.date_medecin = slugify(f" {self.date} {self.consult_code_medecin}")
        self.date_patient = slugify(f"{self.date} {self.consult_num_patient}")
        super().save(*args, **kwargs)
        

    def __str__(self):
        return f"{self.id_consultation}"