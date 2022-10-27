# from django.urls import path, include
# from tutorial_1 import views
#
#
# urlpatterns = [
#     path('addresses/', views.address_list),
#     path('addresses/<int:pk>/', views.address),
#     path('login/',views.login),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     path('',include('tutorial_serializer.urls'))
# ]

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from django.contrib import admin
from config.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api2/',include('inflearnDjango.urls')),
    path('api/', include('api.urls')),
    path('', HomeView.as_view(), name = 'home'),
    path('blog/', include('blog.urls')),
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_URL)