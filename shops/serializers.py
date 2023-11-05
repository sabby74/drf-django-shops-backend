from rest_framework import serializers
from .models import Shops


class ShopsSerializer(serializers.ModelSerializer):
    class Meta:

        model = Shops
        fields = ('id', 'name', 'description', 'sells', 'rating',
                  'created_at', 'updated_at', 'is_OpenSundays')
