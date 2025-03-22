from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from rest_api.models import Municipality
from rest_api.serializers import MunicipalitySerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class MunicipalityViewSet(ModelViewSet):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer
    pagination_class = StandardResultsSetPagination