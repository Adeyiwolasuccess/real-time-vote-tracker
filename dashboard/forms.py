from django import forms 
from .models import Submission

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ["polling_unit", "image", "notes"]
