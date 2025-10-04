from django.contrib import admin
from .models import Note

# Register your models here.

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)
