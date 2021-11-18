from django.contrib import admin
from .models import *


class GroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


class EventsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'done')
    search_fields = ('title', 'date')


class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'done')
    search_fields = ('title', 'date')
    list_editable = ('done',)
    list_filter = ('done', 'date')



admin.site.register(Groups, GroupsAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(Notes, NotesAdmin)


