from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = routers.DefaultRouter()
router.register(r'locations', views.LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('meetups/', views.MeetupAuthenticatedView.as_view(), name='meetups-view'),
    path('api-token-auth/', obtain_auth_token),
]