# generic

from rest_framework import generics
from rest_api.models import employees
from .serializers import AppPostSerializer

class AppPostCrudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = AppPostCrudView
    #queryset     = employees.objects.all()

    def get_queryset(self):
        return employees.objects.all()
    
