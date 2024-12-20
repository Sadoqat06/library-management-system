from rest_framework import serializers
from .models import BookOrder


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BookOrderModel
#         fields = ['name','surname']


class BookOrderModelSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = BookOrder
        fields = ['id','book','customer','rental_date','deadline', 'returned']

class BookOrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookOrder
        fields = ['book', 'deadline']

class BookOrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookOrder
        fields = ['book', 'deadline','returned']