from django.db import models
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    

    def __str__(self):
        return self.name

class Service(models.Model):
    service_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.service_name
    
class SupportTicket(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ]

    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    issue_description = models.TextField(help_text="A detailed description of the issue.")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    technician = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True, blank=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def mark_as_resolved(self):
        self.status = 'Resolved'
        self.resolved_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.id} - {self.client.name} - {self.status}"

    
class Staff(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return {self.name}
    
class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('Credit Card', 'Credit Card'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Gcash', 'Gcash'),
        ('Cash', 'Cash'),
    ]

    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True, blank=True)
    service = models.ForeignKey('Service', on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    payment_date = models.DateTimeField(auto_now_add=True)
    is_successful = models.BooleanField(default=True)
    transaction_id = models.CharField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.transaction_id or 'N/A'} - {self.client.name}"