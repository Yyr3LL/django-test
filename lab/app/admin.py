from django.contrib import admin
from .models import *


class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'money_count',)
    search_fields = ('name',)
    list_filter = ('money_count',)


class MemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'money_count', 'bank')
    search_fields = ('full_name',)
    list_filter = ('money_count', 'bank')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('value', 'date', 'member',)
    search_fields = ('date',)
    list_filter = ('date', 'member',)


admin.site.register(Bank, BankAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Transaction, TransactionAdmin)
