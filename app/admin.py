from django.contrib import admin
from app.models import LegalSufficiency
import reversion

@admin.register(LegalSufficiency)
class LegalSufficiencyAdmin(reversion.VersionAdmin):
    pass
