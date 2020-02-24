# REST_ListAPIView_Demo

  1. install `djangorestframework`, `markdown`, `django-filter`.
  2. Show the models.
  3. Go to the admin page to show the models, then add them to the `admin.py`.
  4. Create a `ListApiView` for the hotels where only the hotel name will be shown(serializer).
  5. Create a `ListApiView` for bookings where only upcoming bookings will be shown:
      * in the queryset `check_in__gte=datetime.today()`
