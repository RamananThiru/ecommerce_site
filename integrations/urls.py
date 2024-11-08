from django.urls import path
from .api import views
from integrations.api.views import get_cat_fact


urlpatterns = [
    path('api/get_cat_fact/', get_cat_fact, name='get_cat_fact'),
]
