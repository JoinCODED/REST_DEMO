from datetime import datetime

from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView
)

from .models import Hotel, Booking
from .serializers import (
    HotelSerializer,
    BookingSerializer,
    BookingDetailSerializer,
    BookingUpdateSerializer,
    BookingCreateSerializer,
    RegisterSerializer
)


class HotelList(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class BookingList(ListAPIView):
    queryset = Booking.objects.filter(check_in__gt=datetime.today())
    serializer_class = BookingSerializer


class BookingDetailView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"


class BookingUpdateView(RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingUpdateSerializer
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"


class BookingDeleteView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"


class BookingCreateView(CreateAPIView):
    serializer_class = BookingCreateSerializer

    def perform_create(self, serializer):
        hotel_id = self.kwargs.get("hotel_id")
        hotel_object = Hotel.objects.get(id=hotel_id)
        serializer.save(hotel=hotel_object, user=self.request.user)

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
