from django.contrib import admin
from organisation.models import *

# Register your models here.
admin.site.register(Organisation)
admin.site.register(Member)
admin.site.register(Project)
admin.site.register(ProjectCategory)
