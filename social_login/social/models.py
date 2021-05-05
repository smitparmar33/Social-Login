from django.db import models

# Create your models here.
from django.db import models

class Account(models.Model):
    email=models.EmailField(primary_key=True)

    def __str__(self):
        return str(self.email)

    def delete(self,*args,**kwargs):
        self.document.delete()
        super().delete(*args,**kwargs)

class Order(models.Model):
    email=models.ForeignKey(Account, on_delete=models.CASCADE)
    order_name = models.CharField(blank=False,max_length=20)
    STATUS_CHOICES = (
        ('delivered', 'DELIVERED'),
        ('pending', 'PENDING'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return str(self.email)

    def delete(self,*args,**kwargs):
        self.document.delete()
        super().delete(*args,**kwargs)