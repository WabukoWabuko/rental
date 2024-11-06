# rental/forms.py
from django import forms
from .models import Booking, RentPayment, Complaint, Chat

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_date', 'end_date']
        
class RentPaymentForm(forms.ModelForm):
    class Meta:
        model = RentPayment
        fields = ['amount', 'payment_method']

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['description']

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['message']

class PropertyForm(forms.ModelForm):
    class Meta:
        # model = Property
        fields = ['property_type', 'address', 'price', 'description', 'availability', 'image']