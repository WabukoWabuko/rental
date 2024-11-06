from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    """
    Custom user model for handling different roles: tenant, landlord, and admin.
    Extends the default Django user model.
    """
    ROLE_CHOICES = (
        ('tenant', 'Tenant'),
        ('landlord', 'Landlord'),
        ('admin', 'Admin'),
    )
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    password_hash = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} ({self.role})"


class Property(models.Model):
    """
    Property model representing rental properties listed by landlords.
    """
    PROPERTY_TYPE_CHOICES = (
        ('apartment', 'Apartment'),
        ('house', 'House'),
    )
    landlord = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    address = models.CharField(max_length=255)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.property_type.title()} at {self.address}"


class Booking(models.Model):
    """
    Booking model for tracking booking requests made by tenants for properties.
    """
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='bookings')
    date_booked = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Booking for {self.property} by {self.tenant}"


class RentPayment(models.Model):
    """
    RentPayment model to handle rent payments made by tenants.
    """
    PAYMENT_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES)
    payment_method = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Payment of {self.amount} for {self.property} by {self.tenant}"


class Complaint(models.Model):
    """
    Complaint model to handle complaints and requests from tenants.
    """
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
    )
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='complaints')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='complaints')
    description = models.TextField()
    date_filed = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Complaint by {self.tenant} for {self.property}"


class Chat(models.Model):
    """
    Chat model for tenant interactions within a specific property.
    """
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='chats')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat from {self.sender} in {self.property}"


class HouseAvailability(models.Model):
    """
    HouseAvailability model to store property availability based on location.
    """
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='availability_checks')
    location_bandwidth = models.IntegerField()  # Proximity range for tenant
    availability = models.BooleanField(default=True)
    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Availability check for {self.property} - {'Available' if self.availability else 'Unavailable'}"
