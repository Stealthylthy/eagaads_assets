from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .models import Department,Asset,Assignment,Maintenance

class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Role Info', {'fields': ('role', 'department')}),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Department)
admin.site.register(Asset)
admin.site.register(Assignment)
admin.site.register(Maintenance)

