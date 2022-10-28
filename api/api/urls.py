from django.contrib import admin
from django.urls import path, include
from vendors.views import VendorViewSet
from products.views import ProductsViewSet
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'vendors',VendorViewSet)
router.register(r'products',ProductsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
