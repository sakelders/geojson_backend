from rest_framework.viewsets import ModelViewSet
from rest_framework_gis.pagination import GeoJsonPagination

from rest_api.models import Municipality
from rest_api.serializers import MunicipalitySerializer


class MunicipalityPagination(GeoJsonPagination):
    page_size = 25
    page_size_query_param = 'page_size'


class MunicipalityViewSet(ModelViewSet):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer
    pagination_class = MunicipalityPagination