from django.urls import path
from .views import ShopsList, ShopsDetail
from users.views import UsersList


urlpatterns = [
    path('shops/', ShopsList.as_view(), name='shops_list'),
    path('shops/<int:pk>/', ShopsDetail.as_view(), name='shops_detail'),
    path('users/', UsersList.as_view(), name='user_list'),

]