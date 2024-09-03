from django.urls import path,include
from api.views import ContectViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'contacts',ContectViewSet)


urlpatterns = [
    path('', include(router.urls)),
]