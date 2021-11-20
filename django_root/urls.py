"""django_root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django_root import views


# TODO (low priority): Somehow give this file a functional app_name (app_name='name' doesn't work)
urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),  # TODO (low priority): Add name='admin' once this file has a functional app_name
    path('accounts/', include('accounts.urls')),  # TODO (medium priority): Implement the templates for this
    path('administrator/', include('administrator.urls')),
    path('applicant/', include('applicant.urls')),
    path('homepage_redirect', views.homepage_redirect),
]