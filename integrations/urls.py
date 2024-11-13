from django.urls import path
from .api import views
from integrations.api.views import get_cat_fact, save_alert_cat_info


urlpatterns = [
    path('api/get_cat_fact/', get_cat_fact, name='get_cat_fact'),
    path('api/save_alert_cat_info/', save_alert_cat_info, name='save_alert_cat_info')
]
