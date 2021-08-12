from django.contrib import admin
from .models import Gymnast, RegisteredAparatus, CompetitionInformation

# Register your models here.
@admin.register(Gymnast)
class GymnastAdmin(admin.ModelAdmin):
    pass

@admin.register(RegisteredAparatus)
class RegisteredAparatusAdmin(admin.ModelAdmin):
    pass

@admin.register(CompetitionInformation)
class CompetitionInformationAdmin(admin.ModelAdmin):
    pass