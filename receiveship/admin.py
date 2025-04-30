from django.contrib import admin

# Register your models here.
from .models import ReceiverShipCase


@admin.register(ReceiverShipCase)
class ReceiverShipCaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'court')
    list_filter = ('status',)
 