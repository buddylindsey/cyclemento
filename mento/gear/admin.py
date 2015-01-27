from django.contrib import admin

from gear.models import Gear, Compontent


class GearAdmin(admin.ModelAdmin):
    pass


class CompontentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Gear, GearAdmin)
admin.site.register(Compontent, CompontentAdmin)
