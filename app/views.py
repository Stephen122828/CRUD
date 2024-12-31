from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import SupportTicket, Client, Staff, Payment
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Client, Service, SupportTicket, Staff, Payment
from .forms import ClientForm, SupportTicketForm, StaffForm, PaymentForm







class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class ServicesPageView(TemplateView):
    template_name = 'app/services.html'
    
   
class ClientListView(ListView):
    model = Client
    template_name = 'app/client_list.html'
    context_object_name = 'clients'

class ClientDetailView(DetailView):
    model = Client
    template_name = 'app/client_detail.html'
    context_object_name = 'client'

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'app/client_form.html'
    success_url = reverse_lazy('client_list')

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'app/client_form.html'
    success_url = reverse_lazy('client_list')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'app/client_confirm_delete.html'
    success_url = reverse_lazy('client_list')


class SupportTicketListView(ListView):
    model = SupportTicket
    template_name = 'app/supportticket_list.html'
    context_object_name = 'tickets'

class SupportTicketCreateView(CreateView):
    model = SupportTicket
    form_class = SupportTicketForm
    template_name = 'app/supportticket_form.html'
    success_url = reverse_lazy('supportticket_list')

class SupportTicketUpdateView(UpdateView):
    model = SupportTicket
    form_class = SupportTicketForm
    template_name = 'app/supportticket_form.html'
    success_url = reverse_lazy('supportticket_list')

class SupportTicketDeleteView(DeleteView):
    model = SupportTicket
    template_name = 'app/supportticket_confirm_delete.html'
    success_url = reverse_lazy('supportticket_list')


class StaffListView(ListView):
    model = Staff
    template_name = 'app/staff_list.html'
    context_object_name = 'staff'

class StaffCreateView(CreateView):
    model = Staff
    form_class = StaffForm
    template_name = 'app/staff_form.html'
    success_url = reverse_lazy('staff_list')

class StaffUpdateView(UpdateView):
    model = Staff
    form_class = StaffForm
    template_name = 'app/staff_form.html'
    success_url = reverse_lazy('staff_list')

class StaffDeleteView(DeleteView):
    model = Staff
    template_name = 'app/staff_confirm_delete.html'
    success_url = reverse_lazy('staff_list')


class PaymentListView(ListView):
    model = Payment
    template_name = 'app/payment_list.html'
    context_object_name = 'payments'

class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'app/payment_form.html'
    success_url = reverse_lazy('payment_list')

class PaymentUpdateView(UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'app/payment_form.html'
    success_url = reverse_lazy('payment_list')

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'app/payment_confirm_delete.html'
    success_url = reverse_lazy('payment_list')



