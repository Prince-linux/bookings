from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from bookings.utils import validate_data

from .models import Bookings

from bookings.forms.bookings_form import BookingsForm

# Create your views here.


def index(request):
    bookings = Bookings.objects.all()
    return render(request, 'bookings/index.html', {'bookings': bookings})


def new_booking(request):
    bookings_form = BookingsForm()
    return render(request, 'bookings/new_booking.html', {'form': bookings_form})


def save_booking(request):
    bookings_form = BookingsForm(request.POST)
    if bookings_form.is_valid():

        new_booking = Bookings()
        new_booking.name_of_booking = bookings_form.cleaned_data['name_of_booking']
        new_booking.price_of_booking = bookings_form.cleaned_data['price_of_booking']
        new_booking.available = bookings_form.cleaned_data['available']
        # new_booking.image = bookings_form.cleaned_data['image']
        new_booking.save()
        ok, msg = validate_data(new_booking.name_of_booking, new_booking.price_of_booking, new_booking.available)
        if not ok:
            for m in msg:
                messages.warning(request, m)

            return redirect('addBooking')
        else:
            messages.success(request, "Creation of Booking successful!")
            return redirect('main-view')

    else:
        messages.warning(request, "Please fill in the correct details")
        return render(request, 'bookings/new_booking.html', {'form': bookings_form})


def create_booking(self):
    return HttpResponseRedirect('/create_new/')


def edit_booking(request, booking_id):
    booking = Bookings.objects.get(pk=booking_id)
    params = {'name_of_booking': booking.name_of_booking,
              'price_of_booking': booking.price_of_booking,
              'available': booking.available
              # 'image': bookings.image
              }
    bookings_form = BookingsForm(initial=params)
    return render(request, 'bookings/edit_booking.html', {'bookings': booking, 'form': bookings_form})


def update_booking(request, booking_id):
    booking = Bookings.objects.get(pk=booking_id)
    bookings_form = BookingsForm(request.POST)
    if bookings_form.is_valid():

        new_booking = Bookings()
        new_booking.name_of_booking = bookings_form.cleaned_data['name_of_booking']
        new_booking.price_of_booking = bookings_form.cleaned_data['price_of_booking']
        new_booking.available = bookings_form.cleaned_data['available']
        # new_booking.image = bookings_form.cleaned_data['image']
        new_booking.save()
        return HttpResponseRedirect('/index/')

    else:
        return render(request, 'bookings/edit_booking.html', {'bookings': booking, 'form': bookings_form})