from django.urls import path, include
from tutorial_1 import views


urlpatterns = [
    path(r'^addresses/', views.address_list),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]