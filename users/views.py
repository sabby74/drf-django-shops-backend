from rest_framework import generics
from .models import User
from .serializers import UsersCreateSerializer

# Create your views here.


class UsersList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


