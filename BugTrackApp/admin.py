from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from BugTrackApp.models import custom_user, bug_ticket


admin.site.register(custom_user, UserAdmin)
admin.site.register(bug_ticket)