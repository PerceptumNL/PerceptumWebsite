from django.contrib import admin
from organisation.models import *

class OrganisationAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('active', )}),
        ('About', {'fields': (
            'name', 'slogan', 'tagline', 'logo', 'description')}),
        ('Contact', {'fields': ('phone', 'address', 'email', 'timezone')}),
        ('Social networks', {'fields': (
            'facebook', 'twitter', 'linkedin', 'youtube', 'pinterest')})
    )

class MemberAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('active', )}),
        ('About', {'fields': (
            'name', 'tagline', 'description', 'email', 'img')}),
        ('Social networks', {'fields': (
            'facebook', 'twitter', 'linkedin', 'youtube', 'pinterest')})
    )

class MemberInlineAdmin(admin.TabularInline):
    model = Member.projects.through
    extra = 1
    verbose_name = "Member"
    verbose_name_plural = "Members"

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('active', )}),
        ('About', {'fields': ('title', 'description', 'categories')}),
        ('Images', {'fields': ('small_img', 'large_img')}),
        ('Links', {'fields': ('website', 'repository')}),
    )
    inlines = (MemberInlineAdmin,)
    model = Project

# Register your models here.
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory)
