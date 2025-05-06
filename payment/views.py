from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from sslcommerz_lib import SSLCOMMERZ
import uuid
from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import redirect

from .serializers import CheckoutSerializer, OrderitemSerializer
from .models import Checkout, Orderitem


from product.models import Cart 
from django.utils import timezone

class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class =CheckoutSerializer


class OrderitemViewSet(viewsets.ModelViewSet):
    queryset = Orderitem.objects.all()
    serializer_class = OrderitemSerializer



    
class PaymentViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'])
    def create_payment(self, request):

        user_id = request.data.get('user')
        orderitem_id = request.data.get("orderitem_id")
        email = request.data.get('email')
        name = request.data.get("name")
        total_amount = request.data.get('total_amount')

        user = None
        if user_id:
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return Response({"error": "Invalid user ID"}, status=400)

        tran_id = str(uuid.uuid4())[:10]

        settings = {
            'store_id': 'arman679a8128a9e35',
            'store_pass': 'arman679a8128a9e35@ssl',
            'issandbox': True,
        }

        sslcz = SSLCOMMERZ(settings)

        post_body = {
            'total_amount': total_amount,
            'currency': "BDT",
            'tran_id': tran_id,
            'success_url': f"https://glamify-backend-tp2c.onrender.com/payment/success/{orderitem_id}/",
            'fail_url': "https://glamify-backend-tp2c.onrender.com/payment/failed/",
            'cancel_url': "https://glamify-backend-tp2c.onrender.com/payment/cancel/",
            'emi_option': 0,
            'cus_name': "arman",
            'cus_email': "arman@gmail.com",
            'cus_phone': "1908349238",
            'cus_add1': "Mirpur, Dhaka",
            'cus_city': "Dhaka",
            'cus_country': "Bangladesh",
            'shipping_method': "NO",
            'multi_card_name': "10304040",
            'num_of_item': 1,
            'product_name': "Test Product",
            'product_category': "Test Category",
            'product_profile': "general",
        }

        try:
            response = sslcz.createSession(post_body)
            if 'GatewayPageURL' not in response:
                return Response({"error": "Payment session creation failed", "details": response}, status=400)
            return Response({'payment_url': response['GatewayPageURL']})
        except Exception as e:
            return Response({"error": "Payment processing failed", "details": str(e)}, status=500)


    
# class PaymentSuccessAPI(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request, orderitem_id):  

#         orderitem_id= Orderitem.objects.filter(id=orderitem_id).first()

#         if orderitem_id:
#             orderitem_id.is_paid = True
#             orderitem_id.save()
#             return redirect("https://glamify-frontend-site.netlify.app/order_details.html")
        
#         return Response({"error": "Order not found"}, status=404)


class PaymentSuccessAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request, orderitem_id):  
        orderitem = Orderitem.objects.filter(id=orderitem_id).first()

        if not orderitem:
            return Response({"error": "Order not found"}, status=404)

        user = orderitem.user

        # 1️⃣ কার্ট থেকে সব আইটেম নিয়ে Orderitem এ কপি করা
        cart_items = Cart.objects.filter(user=user)
        if not cart_items.exists():
            return Response({"error": "Cart is empty"}, status=400)

        for cart in cart_items:
            Orderitem.objects.create(
                user=user,
                checkout=orderitem.checkout,
                product_name=cart.product,
                quantity=cart.quantity,
                status="Scucess",
                created_at=timezone.now(),
                is_paid=False
            )

        # 2️⃣ কার্ট ক্লিয়ার করা
        # cart_items.delete()

        # 3️⃣ প্রথম যেই orderitem এসেছিলো, সেটা paid করে দাও
        orderitem.is_paid = True
        orderitem.save()

        # 4️⃣ রিডাইরেক্ট করো
        return redirect("https://glamify-frontend-site.netlify.app/order_details.html")


class PaymentFailedAPI(APIView):
    permission_classes = [AllowAny]  

    def post(self, request):
        return redirect("https://glamify-frontend-site.netlify.app/order_details.html")


class PaymentCancelAPI(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        return redirect("https://glamify-frontend-site.netlify.app/order_details.html")





