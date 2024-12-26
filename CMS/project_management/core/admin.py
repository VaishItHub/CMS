from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Client, Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'client', 'start_date', 'end_date')
    search_fields = ('name', 'client__name')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name',)

admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin)
