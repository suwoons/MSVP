"""my_project URL Configuration

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
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from two_factor.urls import urlpatterns as tf_urls
from two_factor.views import LoginView
from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('password/', include('password.urls')),
    path('about/', TemplateView.as_view(template_name='about.html'), name = 'about'),
    path('api/v1/', include('api.urls')),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path(r'', include(tf_urls)),
    url(r'', include(tf_twilio_urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
