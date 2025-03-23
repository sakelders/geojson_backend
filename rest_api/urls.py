from django.urls import path
from rest_framework.routers import DefaultRouter

from rest_api import views

router = DefaultRouter()
router.register('municipalities', views.MunicipalityViewSet, basename='municipality')

urlpatterns = router.urls
urlpatterns += [path('municipalities/', views.MunicipalitiesListCreateView.as_view(), name='municipality-list')]