from django.contrib import admin

from .models import Meetup

# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')
    list_filter = ('title', 'slug')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Meetup, MeetupAdmin)