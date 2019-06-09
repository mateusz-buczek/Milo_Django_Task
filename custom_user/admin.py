from django.contrib import admin
from custom_user.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'birth_date', 'random_number']
    fieldsets = [
        (None, {'fields': ['user', 'birth_date',]}),
        ('Random number', {'fields': ['random_number'], 'classes': ['collapse']}),
    ]
# random number is hidden in detail view, as it is supposed be to generated upon creation - why change?


admin.site.register(Profile, ProfileAdmin)
