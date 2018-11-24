#adapted from https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from . models import Profile
from order.models import Order, OrderItem

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.address = form.cleaned_data.get('address')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.postcode = form.cleaned_data.get('postcode')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})


def account_info(request):
    current_user = request.user
    profile_details = Profile.objects.filter(user_id=current_user.id)
    orders = Order.objects.filter(user_id=request.user.id)
    order_info_list = []
    for order in orders:
        order_info_list += OrderItem.objects.filter(order_id=order.id)
    template = 'account/details.html'
    context = {
        'account_details': current_user,
        'profile_details': profile_details,
        'orders': orders,
        'order_info_list': order_info_list,
    }
    return render(request, template, context)


