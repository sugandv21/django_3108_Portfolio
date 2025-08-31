from django.contrib import admin
from .models import Project, Skill, ContactMessage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "link")
    search_fields = ("title", "description")
    list_filter = ("title",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "proficiency_level")
    search_fields = ("name",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "message")
    list_filter = ("created_at",)
    readonly_fields = ("name", "email", "message", "created_at") 
