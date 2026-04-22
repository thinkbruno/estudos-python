"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from backend.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("password/", password_view),
    path("age/", age_view),
    path("battery/", battery_view),
    path("currency/", currency_view),
    path("operator/", operator_view),
    path("download/", download_view),
    path("json/", json_view),
    path("pc-info/", pc_info_view),
    path("pdf/", pdf_view),
    path("qrcode/generate/", qrcode_generate_view),
    path("qrcode/read/", qrcode_read_view),
    path("speedtest/", speedtest_view),
]
