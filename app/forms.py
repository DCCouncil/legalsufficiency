from django import forms
from app.models import LegalSufficiency

class LegalSufficiencyForm(forms.ModelForm):
    CHOICES = [('draft','Draft'), ('review','Review')]
    # status = forms.CharField(max_length=10, widget=forms.Select(choices=CHOICES))
    class Meta:
        model = LegalSufficiency
        exclude = ['id','attorney','publish_date', 'slug']