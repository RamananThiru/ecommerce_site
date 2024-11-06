from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

class ProductConfig(AppConfig):
    # from products.models import Product
    name = 'products'

    def ready(self):
        import products.signals  # Import signals to ensure they're registered
