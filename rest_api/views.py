from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework_gis.filters import InBBoxFilter
from rest_framework_gis.pagination import GeoJsonPagination

from rest_api.models import Municipality
from rest_api.serializers import MunicipalitySerializer


class MunicipalityPagination(GeoJsonPagination):
    page_size = 100
    page_size_query_param = 'page_size'


class MunicipalityViewSet(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer


class MunicipalitiesListCreateView(ListAPIView, CreateAPIView):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer
    bbox_filter_field = 'polygons'
    filter_backends = (InBBoxFilter,)
    bbox_filter_include_overlapping = True
    pagination_class = MunicipalityPagination