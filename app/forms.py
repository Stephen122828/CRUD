from django import forms
from .models import Client, SupportTicket, Staff, Payment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


# Client Form
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone_number']


# SupportTicket Form
class SupportTicketForm(forms.ModelForm):
    class Meta:
        model = SupportTicket
        fields = ['client', 'issue_description', 'technician']

# Staff Form
class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'email', 'phone_number']

# Payment Form
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['client', 'service', 'amount', 'payment_method', 'is_successful', 'transaction_id']