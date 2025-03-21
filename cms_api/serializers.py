from rest_framework import serializers
from .models import WebPage, PageSection, Country, City, Vendor, Device, Lead, WalkIn

class WebPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebPage
        fields = '__all__'

class PageSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageSection
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

class WalkInSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalkIn
        fields = '__all__'
