from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from .models import Vendor, WebPage, Device, Lead, WalkIn, Country, City
from .serializers import (
    WebPageSerializer, DeviceSerializer, LeadSerializer, WalkInSerializer, 
    CountrySerializer, CitySerializer ,  VendorSerializer 
)

import logging

logger = logging.getLogger(__name__)
# API to list all available devices
class DeviceListAPIView(generics.ListAPIView):
    queryset = Device.objects.filter(status=True)
    serializer_class = DeviceSerializer

# API to create a new device
class DeviceCreateAPIView(generics.CreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


# API to handle lead capture and generate a token
class LeadCaptureAPIView(APIView):
    def post(self, request):
        try:
            serializer = LeadSerializer(data=request.data)
            if serializer.is_valid():
                with transaction.atomic():
                    lead = serializer.save()
                    vendor = Vendor.objects.filter(city=lead.city).first()
                    device = Device.objects.filter(status=True).first()
                    
                    if not vendor or not device:
                        return Response({'error': 'No vendor or device available for this city'}, status=400)
                    
                    walk_in = WalkIn.objects.create(
                        lead=lead,
                        vendor=vendor,
                        device=device,
                        currency='USD',
                        offer_price=100.00
                    )
                    
                    try:
                        send_mail(
                            'Walk-in Token Generated',
                            f'Hello {lead.name}, your token number is {walk_in.token_number}.',
                            'noreply@example.com',
                            [lead.email],
                            fail_silently=False,
                        )
                    except Exception as e:
                        logger.error(f"Email sending failed: {e}")
                        return Response({'error': 'Lead captured, but email could not be sent.'}, status=500)
                    
                    return Response({'message': 'Lead captured successfully!', 'token_number': walk_in.token_number})
            return Response(serializer.errors, status=400)
        except ObjectDoesNotExist as e:
            logger.error(f"Object not found: {e}")
            return Response({'error': 'Invalid reference to city or country.'}, status=400)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return Response({'error': 'An unexpected error occurred. Please try again.'}, status=500)



'''class LeadCaptureAPIView(APIView):
    def post(self, request):
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            lead = serializer.save()
            # Create a walk-in record and generate a token
            walk_in = WalkIn.objects.create(
                lead=lead,
                vendor=lead.city.vendor_set.first(),  # Assigning first vendor in the city
                device=Device.objects.filter(status=True).first(),  # Assign first available device
                currency='USD',
                offer_price=100.00  # Example static price, can be updated as needed
            )
            
            # Send email to lead and vendor
            send_mail(
                'Walk-in Token Generated',
                f'Hello {lead.name}, your token number is {walk_in.token_number}.',
                'noreply@example.com',
                [lead.email],
                fail_silently=False,
            )
            
            return Response({
                'message': 'Lead captured successfully!',
                'token_number': walk_in.token_number
            })
        return Response(serializer.errors, status=400)'''
    

# API to retrieve a webpage
class WebPageDetailAPIView(generics.RetrieveAPIView):
    queryset = WebPage.objects.all()
    serializer_class = WebPageSerializer


# API to list and create vendors
class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

# API to list and create countries
class CountryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

# API to list and create cities
class CityListCreateAPIView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

# API to list all walk-ins
class WalkInListAPIView(generics.ListAPIView):
    queryset = WalkIn.objects.all()
    serializer_class = WalkInSerializer
