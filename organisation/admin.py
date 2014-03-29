from django.contrib import admin
from organisation.models import *

class OrganisationAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': (
            'name', 'slogan', 'tagline', 'logo', 'description')}),
        ('Contact', {'fields': ('phone', 'address', 'email', 'timezone')}),
        ('Social networks', {'fields': (
            'facebook', 'twitter', 'linkedin', 'youtube', 'pinterest')})
    )

# Register your models here.
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Member)
admin.site.register(Project)
admin.site.register(ProjectCategory)
