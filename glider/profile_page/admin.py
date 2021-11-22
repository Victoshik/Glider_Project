from .models import *

from django.contrib import admin


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'birth_date', 'gender')
    search_fields = ('user',)


admin.site.register(Profile, ProfileAdmin)