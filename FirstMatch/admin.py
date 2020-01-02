from django.contrib import admin
from FirstMatch.models import Adelphoi_Mapping,ModelTests
# Register your models here.
admin.site.register(ModelTests)
admin.site.register(Adelphoi_Mapping)


# @admin.register(Adelphoi_Mapping)
# class AdelphoiMappoingAdmin(admin.ModelAdmin):
#     list_display = ('program','program_name', 'gender')
#     search_fields = ('program',)