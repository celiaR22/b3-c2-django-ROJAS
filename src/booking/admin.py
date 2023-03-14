from django.contrib import admin
from booking.models import Cart, Reservation, pilotEvent

# Register your models here.
admin.site.register(pilotEvent)
admin.site.register(Reservation)
admin.site.register(Cart)