from django.contrib import admin

# Register your models here.
from .models import Join


class JoinAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'friend','timestamp', 'update']
    class meta:
        model = Join

admin.site.register(Join, JoinAdmin)

