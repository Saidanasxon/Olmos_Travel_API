from django.urls import path, include
from .views  import *
from rest_framework import routers

app_name = 'my_app'

router = routers.DefaultRouter()
router.register('tour_classes', Tour_classViewSet),
router.register('tours', TourViewSet),

urlpatterns = [
    path('my_app/', include(router.urls)),
]