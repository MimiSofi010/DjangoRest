from django.contrib import admin
from passenger.models import Passenger
# Register your models here.

class PassengerAdmin(admin.ModelAdmin):
    fields = ('firstName', 'lastName', 'rewardPoints', 'email')
    list_display = ('id', 'firstName', 'lastName', 'rewardPoints', 'email')
    list_filter = ('lastName',)

admin.site.register(Passenger, PassengerAdmin)