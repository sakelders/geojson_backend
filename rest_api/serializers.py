from rest_framework import serializers

from rest_api.models import Municipality


class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = ['name', 'polygons']