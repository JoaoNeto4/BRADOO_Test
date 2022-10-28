from rest_framework import viewsets
from .models import Products
from .serializers import ProductsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all().order_by('id')
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id', 'name', 'code', 'price', 'vendor']
    search_fields = ['id', 'name', 'code', 'price', 'vendor']
    
    