from django.db import models
from django.contrib.sites.models import Site
from django.contrib.auth.models import User

# Extend Site Model
class WebPage(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    allowed_devices = models.ManyToManyField('Device', blank=True)

class PageSection(models.Model):
    page = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='sections/')
    html_content = models.TextField()
    order = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

# Location Models
class Country(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

# Vendor Model
class Vendor(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    managed_by = models.ForeignKey(User, on_delete=models.CASCADE)

# Device Model
class Device(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='devices/')
    currency = models.CharField(max_length=10)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    sourced_from = models.ManyToManyField(Vendor)
    status = models.BooleanField(default=True)

# Lead Model
class Lead(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In-progress', 'In-progress'),
        ('Converted', 'Converted'),
        ('Rejected', 'Rejected')
    ]
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    referral_code = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

# Walk-in Model with Token Number Auto-Increment
class WalkIn(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    currency = models.CharField(max_length=10)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    walk_in_datetime = models.DateTimeField(auto_now_add=True)
    token_number = models.PositiveIntegerField(unique=True)

    def save(self, *args, **kwargs):
        if not self.token_number:
            last_token = WalkIn.objects.all().order_by('-token_number').first()
            self.token_number = last_token.token_number + 1 if last_token else 1
        super().save(*args, **kwargs)
