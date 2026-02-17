from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    status_choice = (
        ('pending','Pending'),
        ('completed','Completed'),
        ('cancelled','Cancelled'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    assign_by = models.ForeignKey(
        User,
        on_delete= models.CASCADE,
        related_name='assign_by'
    )
    assign_to = models.ForeignKey(
        User,
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