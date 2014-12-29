from django import forms
from app.models import LegalSufficiency

class LegalSufficiencyForm(forms.ModelForm):
    class Meta:
        model = LegalSufficiency
        exclude = ['id']
