from django.db import models
from django.core.exceptions import ValidationError
import pdb

# Create your models here.

"""
Basic custom validator method. Checks for error and raises exception
"""
    


class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.name == 'test_name':
            raise ValidationError(f"Invalid Name for the product")
        
    def save(self, *args, **kwargs):
        """
        Override save() and call clean() before saving to catch validation errors
        It will be probelamtic if full_clean() is used, clean() might be triggered twice
        """
        self.clean()
        super(Product, self).save(*args, **kwargs)


    def __str__(self):
        return self.name
  
