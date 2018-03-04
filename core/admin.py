from django.contrib import admin

# Register your models here.
from core.models import ProjectRequest


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'phone', 'email','created_at')
    list_filter = ('id',)


admin.site.register(ProjectRequest, ProjectAdmin)
