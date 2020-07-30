from django.urls import include, path
from rest_framework import routers

from quiz import views

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include('quiz.urls')),
    path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]