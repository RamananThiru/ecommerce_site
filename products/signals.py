# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Product
import pdb


@receiver(post_save, sender=Product)
def after_save_product(sender, instance, created, **kwargs):
    if created:
        print(f"A new product '{instance.name}' has been created.")
    else:
        print(f"The product '{instance.name}' has been updated.")
