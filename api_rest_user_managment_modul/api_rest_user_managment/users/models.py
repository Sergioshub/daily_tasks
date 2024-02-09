from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    email = models.EmailField(unique=True)


class UsersContact(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='contacts')
    country_code = models.CharField(max_length=2)
    phone_number = models.CharField(max_length=15)
    updated_at = models.DateTimeField(default=timezone.now)

    # user = CustomUser.objects.get(id=1)
    # contacts = user.contacts.all()
    
    def __str__(self):
        return f"{self.user.username}'s contacts: {self.country_code}, {self.phone_number}" 

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-updated_at'] 
