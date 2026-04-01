from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        SUPERADMIN = "SUPERADMIN", "Superadmin"

    role = models.CharField(choices=Role.choices, default=Role.ADMIN, max_length=10)

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN

    @property
    def is_superadmin(self):
        return self.role == self.Role.SUPERADMIN
    
    class Meta:
        ordering = ['-pk']


class Student(models.Model):
    class Gender(models.TextChoices):
        ERKAK = "ERKAK", "Erkak"
        AYOL = "AYOL", "Ayol"

    admin = models.ForeignKey(
        "CustomUser",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="kim yaratdi"
    )

    name = models.CharField(max_length=100)
    gender = models.CharField(
        choices=Gender.choices, default=Gender.ERKAK, max_length=50
    )

    year = models.IntegerField()
    faculty = models.CharField(max_length=100, blank=True, null=True)
    direction = models.CharField(max_length=100, blank=True, null=True)
    location = models.TextField()
    number = models.CharField(max_length=15,unique=True)
    parent_number = models.CharField(max_length=15, unique=True)
    telegram_id = models.BigIntegerField(unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return f"{self.name} {self.room}"
    
    class Meta:
        ordering = ['-pk']