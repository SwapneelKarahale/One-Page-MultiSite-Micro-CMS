from django.urls import path
from .views import (
    DeviceListAPIView, DeviceCreateAPIView, LeadCaptureAPIView, WebPageDetailAPIView,
    CountryListCreateAPIView, CityListCreateAPIView, WalkInListAPIView,VendorListCreateAPIView
)

urlpatterns = [
    path('devices/', DeviceListAPIView.as_view(), name='device-list'),
    path('devices/create/', DeviceCreateAPIView.as_view(), name='device-create'),
    path('lead-capture/', LeadCaptureAPIView.as_view(), name='lead-capture'),
    path('webpage/<int:pk>/', WebPageDetailAPIView.as_view(), name='webpage-detail'),
    path('countries/', CountryListCreateAPIView.as_view(), name='country-list-create'),
    path('cities/', CityListCreateAPIView.as_view(), name='city-list-create'),
    path('walkins/', WalkInListAPIView.as_view(), name='walkin-list'),
    path('vendors/', VendorListCreateAPIView.as_view(), name='vendor-list-create'),
]
