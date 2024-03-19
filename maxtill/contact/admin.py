from django.contrib import admin
from .models import Message, Info, Contact

# Register your models here.
admin.site.register(Message)
admin.site.register(Info)
admin.site.register(Contact)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'contenus', 'date_add', 'active')
    list_filter = ('active', 'date_add')
    search_fields = ('nom', 'email','phone', 'contenus')
    actions = ['approve_contact']

    def approve_contact(self, request, queryset):
        queryset.update(active=True)