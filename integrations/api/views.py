from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pdb


from django.http import JsonResponse
from django.conf import settings
from ..services.cat_facts_service import get_random_cat_fact

@api_view(['GET'])
def get_cat_fact(request):
   data = get_random_cat_fact()
   return Response(data)

@api_view(['POST'])
def save_alert_cat_info(request):
   return Response({})

