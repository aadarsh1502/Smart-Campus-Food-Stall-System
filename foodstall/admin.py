from django.contrib import admin
from .models import FoodItem, TimeSlot, Order

admin.site.register(FoodItem)
admin.site.register(TimeSlot)
admin.site.register(Order)