
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CheckoutViewSet,OrderitemViewSet, PaymentViewSet,  PaymentSuccessAPI, PaymentFailedAPI, PaymentCancelAPI


router = DefaultRouter()
router.register(r'payment', PaymentViewSet, basename='payment')
router.register(r'checkout',CheckoutViewSet, basename='checkout')
router.register(r'orderitem', OrderitemViewSet, basename='Orderitem')

urlpatterns = [
    path('', include(router.urls)),
    path('payment/success/<int:orderitem_id>/', PaymentSuccessAPI.as_view(), name='payment-success'),
    path('payment/failed/', PaymentFailedAPI.as_view(), name='payment-failed'),
    path('payment/cancel/', PaymentCancelAPI.as_view(), name='payment-cancel'),

]

