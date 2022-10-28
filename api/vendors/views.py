from rest_framework import viewsets
from .models import Vendor
from .serializers import VendorSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all().order_by('id')
    serializer_class = VendorSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id', 'name', 'cnpj', 'city']
    search_fields = ['id', 'name', 'cnpj', 'city']
