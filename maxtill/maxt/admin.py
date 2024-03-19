from django.contrib import admin
from .models import First, Second, Third, Title, Info

# Register your models here.
admin.site.register(Title)
admin.site.register(First)
admin.site.register(Second)
admin.site.register(Third)
admin.site.register(Info)