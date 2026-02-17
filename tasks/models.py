from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class CustomUser(AbstractUser):
    role_choice = (
        ('senior', 'Senior'),
        ('junior', 'Junior'),
    )
    role = models.CharField(
        choices=role_choice,
        max_length=20,
        default='junior'
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username




class Tasks(models.Model):
    status_choice = (
        ('pending','Pending'),
        ('completed','Completed'),
        ('cancelled','Cancelled'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    assign_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
        related_name='assign_by'
    )
    assign_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name='assign_to' 
    )
    status = models.CharField(
        max_length=20,
        choices=status_choice,
        default='pending'
    )

    def __str__(self):
        return self.title