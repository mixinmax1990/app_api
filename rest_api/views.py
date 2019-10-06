from django.shortcuts import render

#HTTP imports for API requests
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employees
from .serializers import employeesSerializers

# Create your views here.

class employeeList(APIView):

    def get(self, requests):
        employees1= employees.objects.all() # retrieves data
        serializer= employeesSerializers(employees1, many=True) # converts data into JSON
        
        return Response(serializer.data) # Returns JSON data 

    def post(self):
        pass
