from rest_framework import generics
from .models import Shops
from .serializers import ShopsSerializer

# Create your views here.

class ShopsList(generics.ListCreateAPIView):
    queryset = Shops.objects.all()
    serializer_class = ShopsSerializer


class ShopsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shops.objects.all()
    serializer_class = ShopsSerializer
  

    



