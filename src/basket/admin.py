from django.contrib import admin
from basket.models import Basket


class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'count')
    readonly_fields = ('add_datetime',)
    fieldsets = (
        (None, {'fields': ('user', 'phone', 'count', 'add_datetime')}),
    )
    search_fields = ('user__username', 'phone__name', 'phone__brand')
    ordering = ('-add_datetime',)
    list_filter = ('phone__brand', )
    filter_horizontal = ()


admin.site.register(Basket, BasketAdmin)
