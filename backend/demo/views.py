from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt#to avoid 403 error
from django.http import JsonResponse
import json
@csrf_exempt# to avoid 403 error
def greet_api(request):
    if request.method == 'POST':
        # Get the body data (in raw JSON format)
        try:
            data = json.loads(request.body)
            name = data.get('name', '')  # get the name, default to empty string if not found
            if name:
                return JsonResponse({"message": f"Hello, {name}! Welcome to the API!"})
            else:
                return JsonResponse({"error": "No name provided!"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format!"}, status=400)
    return JsonResponse({"error": "Only POST method allowed!"}, status=405)
'''DRF frame work
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class GreetView(APIView):
    def post(self, request):
        name = request.data.get('name')
        if name:
            return Response({'message': f'Hello, {name}!'})
        return Response({'error': 'Name not provided'}, status=status.HTTP_400_BAD_REQUEST)'''