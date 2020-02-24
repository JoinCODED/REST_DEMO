"""pooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from hotels import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hotels/', views.HotelList.as_view()),
    path('hotels/<int:hotel_id>/bookings/create/', views.BookingCreateView.as_view()),

    path('bookings/', views.BookingList.as_view()),
    path('bookings/<int:booking_id>/', views.BookingDetailView.as_view()),
    path('bookings/<int:booking_id>/update/', views.BookingUpdateView.as_view()),
    path('bookings/<int:booking_id>/delete/', views.BookingDeleteView.as_view()),

    # Authentication
    path('login/', TokenObtainPairView.as_view()),
    path('register/', views.RegisterView.as_view()),
]
