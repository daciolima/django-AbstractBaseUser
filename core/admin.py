from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'created_at', 'updated_at', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'created_at', 'updated_at')
    ordering = ('email',)

    fieldsets = (
        ('Conta', {'fields': ('email', 'password')}),
        ('Informação Pessoal', {'fields': ('first_name', 'last_name',)}),
        ('Permissões', {'fields': ('is_staff', 'is_admin', 'is_active')}),
        ('Histórico', {'fields': ('created_at', 'updated_at',)}),
    )
    add_fieldsets = (
        ('None', {'classes': ('wide',),
                  'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'groups',),
                  }),
    )

    filter_horizontal = ('groups',)
    list_filter = ('is_active', 'is_staff', 'is_admin', 'is_superuser', 'groups')


admin.site.register(Account, AccountAdmin)



