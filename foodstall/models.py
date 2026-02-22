from django.db import models
from django.contrib.auth.models import User

class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def __str__(self):
        return f"{self.start_time} - {self.end_time}"

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.food_item.price * self.quantity

    def __str__(self):
        return f"{self.student.username} - {self.food_item.name}"