from django.db import models
from django.contrib.auth.models import User


class Lead(models.Model):
    STATUS_CHOICES = [
    ('NEW', 'New'),
    ('CONTACTED', 'Contacted'),
    ('INTERESTED', 'Interested'),
    ('QUOTED', 'Quotation Sent'),
    ('NEGOTIATION', 'Negotiation'),
    ('WON', 'Closed Won'),
    ('LOST', 'Closed Lost')
    ]


    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    location = models.CharField(max_length=100)


    product_category = models.CharField(max_length=50)
    product_model = models.CharField(max_length=100)
    price_range = models.CharField(max_length=50)



    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW')


    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name