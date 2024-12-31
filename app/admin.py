from django.contrib import admin
from .models import Client, Service, SupportTicket, Staff, Payment

admin.site.register(Client)
admin.site.register(Service)
admin.site.register(SupportTicket)
admin.site.register(Staff)
admin.site.register(Payment)