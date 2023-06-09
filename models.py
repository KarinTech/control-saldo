from django.db import models

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_received = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
