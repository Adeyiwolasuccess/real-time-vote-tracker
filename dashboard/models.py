from django.conf import settings
from django.db import models


class Party(models.Model):
    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=10, unique=True)
    logo = models.ImageField(upload_to="party_logos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.acronym


# Polling Unit Model
class PollingUnit(models.Model):
    name =models.CharField(max_length=225)
    code = models.CharField(max_length=50, unique=True)
    state = models.CharField(max_length=100)
    lga = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.code})"
    
# Submission Model
class Submission(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("verified", "Verified"),
        ("flagged", "Flagged"),
    ]

    polling_unit = models.ForeignKey(
        PollingUnit,
        on_delete=models.CASCADE,
        related_name="submissions"
    )
    
    submitted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="submissions",
    )

    image = models.ImageField(upload_to="result_sheets/")
    notes = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return f"Submission {self.id} - {self.polling_unit.code}"