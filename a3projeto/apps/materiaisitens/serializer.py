from .models import Materiaisitens
from rest_framework import serializers

class MateriaisitensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materiaisitens
        fields = '__all__'