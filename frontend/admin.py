from django.contrib import admin
from frontend.models import *
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

class BackgroundImageInline(admin.TabularInline):
    model = BackgroundImage
    extra = 1

class TrebleInterfaceAdmin(PolymorphicChildModelAdmin):
    base_model = TrebleInterface
    exclude = ('template',)
    inlines = (BackgroundImageInline,)
    fieldsets = (
        (None, {'fields': (
            'page_title', 'page_description', 'page_icon')}),
        ('Settings', {'fields': (
            'active', 'show_social', 'member_project_filter')}),
        ('Visuals', {'fields': (
            'scrolldown_visual', 'scrolldown_flipped_visual')}),
        ('Text', {'fields': (
            'description_title',
            'members_title', 'members_intro',
            'work_title', 'work_intro',
            'contact_title', 'contact_intro')}),     
        ('Other', {'fields': ('ganalytics_id',)})
    )

class InterfaceAdmin(PolymorphicParentModelAdmin):
    base_model = Interface
    child_models = (
        (TrebleInterface, TrebleInterfaceAdmin),
    )

# Register your models here.
admin.site.register(Interface, InterfaceAdmin)

