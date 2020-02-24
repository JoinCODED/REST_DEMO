from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Hotel, Booking

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'location', 'price_per_night']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "user", "hotel", "check_in"]


class BookingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "user", "hotel", "check_in", "number_of_nights"]


class BookingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["check_in", "number_of_nights"]


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["check_in", "number_of_nights"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["username", "password"]

    # To encrypt password... dis
    def create(self, validated_data):
        username = validated_data.get("username")
        password = validated_data.get("password")
        user = User(username=username)
        user.set_password(password)
        user.save()
        return validated_data


# def some_voew(request):
#     ...
#     if request...
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(user.password)
#             user.save()
