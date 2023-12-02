from .models import Orgao
from rest_framework import serializers

class OrgaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orgao
        fields = '__all__'