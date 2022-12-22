from django.contrib import admin
from .models import MyLogEntry

# Register your models here.

class LogAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(MyLogEntry, LogAdmin)