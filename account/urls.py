from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

from .views import UserListView
from .views import UserDeleteView
from .views import ContactViewSet
from .views import AdminLoginView
from .views import AdminLogoutView

from .views import PasswordChangeAPIView


router=DefaultRouter()
router.register('contact', ContactViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('register/',views.UserRegistrationApiView.as_view(),name='register'),
    path('login/',views.UserLoginApiView.as_view(),name='login'),
    path('logout/',views.UserLogoutApiView.as_view(),name='logout'),
    path('active/<uid64>/<token>',views.activate,name='activate'),
    path('user/', UserListView.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
    path('admin/login/', AdminLoginView.as_view(), name='admin_login'),
    path('admin/logout/', AdminLogoutView.as_view(), name='admin_logout'),
    path('change_password/<int:user_id>/', PasswordChangeAPIView.as_view(), name='change_password'),
]


