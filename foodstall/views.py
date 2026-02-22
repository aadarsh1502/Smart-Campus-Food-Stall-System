from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import FoodItem, TimeSlot, Order
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'foodstall/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'foodstall/register.html', {'form': form})

@login_required
def place_order(request):
    food_items = FoodItem.objects.filter(available=True)
    time_slots = TimeSlot.objects.all()
    message = ''  # To show confirmation or error

    if request.method == 'POST':
        food_id = request.POST.get('food_item')
        time_id = request.POST.get('time_slot')
        quantity = int(request.POST.get('quantity', 1))

        try:
            food = FoodItem.objects.get(id=food_id)
            time_slot = TimeSlot.objects.get(id=time_id)
        except FoodItem.DoesNotExist:
            message = 'Selected food item does not exist.'
        except TimeSlot.DoesNotExist:
            message = 'Selected time slot does not exist.'
        else:
            Order.objects.create(student=request.user, food_item=food, time_slot=time_slot, quantity=quantity)
            message = f'Order placed successfully! {quantity} x {food.name} at {time_slot}.'

    return render(request, 'foodstall/order.html', {
        'food_items': food_items,
        'time_slots': time_slots,
        'message': message
    })

@login_required
def order_history(request):
    orders = Order.objects.filter(student=request.user).order_by('-timestamp')
    return render(request, 'foodstall/order_history.html', {'orders': orders})

from django.contrib.admin.views.decorators import staff_member_required
# from .models import Order

@staff_member_required
def shopkeeper_orders(request):
    orders = Order.objects.all().order_by('-timestamp')
    return render(request, 'foodstall/shopkeeper_orders.html', {'orders': orders})