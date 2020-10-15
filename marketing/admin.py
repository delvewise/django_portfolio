from django.contrib import admin

from .models import Signup, Leads

admin.site.register(Signup)


class LeadsAdmin(admin.ModelAdmin):
    list_display = ('email', 'message',)
    list_filter = ("captured",)
    readonly_fields = ('timestamp',)
    search_fields = ['email']
    fields= ('email', 'message', 'timestamp', 'captured','subject')


admin.site.register(Leads, LeadsAdmin)
