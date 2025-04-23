from rest_framework import viewsets
from .models import Product,Review,Brand
from .serializers import ProductSerializer,ReviewSerializer,BrandSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated
from .models import Cart
from .serializers import CartSerializer



class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter] 
    filterset_fields = ['brand'] 
    search_fields = ['name', 'description'] 

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return JsonResponse({"message": "Product deleted successfully"}, status=204)


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.select_related("user", "product")
    serializer_class = CartSerializer

    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer











