from django.contrib import admin
from app.models import LegalSufficiency

@admin.register(LegalSufficiency)
class LegalSufficiencyAdmin(admin.ModelAdmin):
    pass
