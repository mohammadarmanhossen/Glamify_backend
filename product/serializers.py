from rest_framework import serializers
from .models import Product
from rest_framework import serializers
from .models import Product,Review,Brand
from rest_framework import serializers
from .models import Cart



class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)  
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())  

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'image_url', 'brand', 'brand_name']



class CartSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    product_price = serializers.DecimalField(source="product.price", max_digits=10, decimal_places=2, read_only=True)
    product_image = serializers.CharField(source="product.image_url", read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "user", "product", "quantity", "product_name", "product_price", "product_image"]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields ="__all__"




