from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'grand_total',)

    fields = ('order_number', 'date', 'name',
              'email', 'phone_number', 'country',
              'town_or_city', 'street_address1',
              'street_address2', 'county', 'postcode', 
              'grand_total')

    list_display = ('name', 'order_number', 'date', 
                    )
    search_fields = ('name', 'email', 'order_number',
                    'date',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)