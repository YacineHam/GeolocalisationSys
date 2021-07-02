"""Geolocalisation_System URL Configuration

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
from rest_framework_simplejwt import views as jwt_views
from app.views import *
from app.views import GetRsaKey,StoreAesKey

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('',map,name="map"),
<<<<<<< HEAD
    path('api/current/<int:id>/',get_current_location,name="current"),
=======
    path('current/<int:id>/',get_current_location,name="current"),
>>>>>>> 2306fdd462f0681d84f9c08c5e12c883bd425dda
    path('history/<int:id>/',get_history,name="history"),
    path('rsakey/',GetRsaKey.as_view(),name="rsakey"),
    path('aeskey/',StoreAesKey.as_view(),name="aeskey"),
]
  