from django.contrib import admin
from .models import User, Property, Booking, RentPayment, Complaint, Chat, HouseAvailability

# Register your models here.

admin.site.register(User)
admin.site.register(Property)
admin.site.register(Booking)
admin.site.register(RentPayment)
admin.site.register(Complaint)
admin.site.register(Chat)
admin.site.register(HouseAvailability)
