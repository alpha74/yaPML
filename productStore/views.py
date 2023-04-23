from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from .paginations import ProductListPagination

# Handles Create and List operations
class ProductListCreate(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	pagination_class = ProductListPagination