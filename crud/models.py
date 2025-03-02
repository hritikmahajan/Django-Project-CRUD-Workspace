from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255, default="Unknown")
    email = models.EmailField(unique=True, null=True, blank=True, default="example@example.com") 
    phone_number = models.CharField(max_length=15, unique=True, default="0000000000")  
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    description = models.TextField(blank=True, null=True, default="No description") 
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.name



