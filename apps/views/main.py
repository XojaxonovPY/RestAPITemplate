from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

@api_view(['GET'])
def hello_world(request):
    d={
        'message':'Hello World'
    }
    return JsonResponse(d)
