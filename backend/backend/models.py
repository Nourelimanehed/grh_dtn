from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
#------------------------------------ User 
class CustomUser(AbstractUser):
    SUPER_ADMIN = 'superadmin'
    ADMIN = 'admin'
    USER = 'user'

    ROLE_CHOICES = (
        (SUPER_ADMIN, 'Super Admin'),
        (ADMIN, 'Admin'),
        (USER, 'User'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=USER)

    def __str__(self):
        return self.email

    def is_superadmin(self):
        return self.role == self.SUPER_ADMIN

    def is_admin(self):
        return self.role == self.ADMIN

    def is_user(self):
        return self.role == self.USER

CustomUser._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_user_permissions'

class UserProfile(models.Model):
    SEXE_CHOICES = (
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    )

    STATUS_CHOICES = (
        ('Actif', 'Actif'),
        ('En congé', 'En congé'),
    )

    SERVICE_CHOICES = (
        ('Service de l’informatique', 'Service de l’informatique'),
        ('Service d’exploitation', 'Service d’exploitation'),
        ('Service de l’administration', 'Service de l’administration'),
        ('Service de maintenance', 'Service de maintenance'),
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    numero_telephone = models.CharField(max_length=15, blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)
    date_recrutement = models.DateField(blank=True, null=True)
    adresse = models.TextField(blank=True)
    grade = models.CharField(max_length=50, blank=True)
    echelon = models.CharField(max_length=50, blank=True)
    poste = models.CharField(max_length=50, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, blank=True)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, blank=True)
