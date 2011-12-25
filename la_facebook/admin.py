from django.contrib import admin
from django.conf import settings
from la_facebook.models import UserAssociation

if settings.DEBUG:
    class UserAssociationAdmin(admin.ModelAdmin):
        list_display = ("user", "identifier", "token", "expires")
    admin.site.register(UserAssociation, UserAssociationAdmin)
