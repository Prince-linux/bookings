import datetime

from django import forms

class BookingsForm(forms.Form):
    name_of_booking = forms.CharField(
        max_length=30,
        widget=forms.TextInput({'class': 'form-control'}),
    )

    price_of_booking = forms.CharField(
        max_length=20,
        widget=forms.TextInput({'class': 'form-control'}),
    )
    # date_of_booking = forms.DateTimeField()
    available = forms.BooleanField(required=False,  initial=False, label='Available')
    # image = forms.ImageField()




