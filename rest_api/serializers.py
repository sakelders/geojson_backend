from rest_framework_gis.serializers import GeoFeatureModelSerializer

from rest_api.models import Municipality


class MunicipalitySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Municipality
        geo_field = 'polygons'
        fields = ['name']