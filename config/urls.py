from django.urls import path, include
from tutorial_1 import views


urlpatterns = [
    path('addresses/', views.address_list),
    path('addresses/<int:pk>/', views.address),
    path('login/',views.login),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('',include('tutorial_serializer.urls'))
]