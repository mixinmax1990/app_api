from rest_framework import serializers

from rest_api.models import employees

class AppPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = [
            'id',
            'firstname',
            'lastname'
        ]
