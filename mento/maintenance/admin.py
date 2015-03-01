from django.contrib import admin

from .models import Maintenance


class MaintenanceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Maintenance, MaintenanceAdmin)
