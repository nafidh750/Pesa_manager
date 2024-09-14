# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('Entrepreneur', 'Entrepreneur'),
        ('RevenueOfficer', 'Revenue Authority Officer'),
        ('Investor', 'Investor/Normal User'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    business_name = models.CharField(max_length=100, blank=True, null=True)
    business_owner_name = models.CharField(max_length=100, blank=True, null=True)
    business_location = models.CharField(max_length=100, blank=True, null=True)
    business_registration_number = models.CharField(max_length=50, blank=True, null=True)
    passkey = models.CharField(max_length=50, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class BusinessData(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    capital = models.DecimalField(max_digits=10, decimal_places=2)
    daily_sales = models.DecimalField(max_digits=10, decimal_places=2)
    profit_loss = models.DecimalField(max_digits=10, decimal_places=2)
    performance_graph = models.ImageField(upload_to='performance_graphs/', blank=True, null=True)

    def __str__(self):
        return f"Business owned by {self.owner.user.username}"

class TaxReport(models.Model):
    officer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    business = models.ForeignKey(BusinessData, on_delete=models.CASCADE)
    tax_paid = models.BooleanField(default=False)
    report_date = models.DateField()

class ChatLog(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

class Expenditure(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.description
