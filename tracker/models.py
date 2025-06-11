from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('hod', 'Head of Department'),
        ('staff', 'Staff'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='staff')
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True)  # Optional, for staff and HODs

    def __str__(self):
        return f"{self.username} ({self.role})"


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
class Asset(models.Model):
    STATUS_CHOICES = [
        ('in_use', 'In Use'),
        ('available', 'Available'),
        ('maintenance', 'Under Maintenance'),
        ('retired', 'Retired'),
    ]

    serial_number = models.CharField(max_length=30, unique=True)
    asset_name = models.CharField(max_length=100)
    purchase_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.asset_name} ({self.serial_number})"
class Assignment(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.asset} → {self.staff.username}"
class Maintenance(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    maintenance_date = models.DateField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Maintenance for {self.asset} on {self.maintenance_date}"

