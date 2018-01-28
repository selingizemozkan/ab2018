from django.contrib import admin
from election.profile.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name' , 'email')
admin.site.register(UserProfile, UserProfileAdmin)