"""ActiveCity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from ACity import settings
from AcCitizen import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', TemplateView.as_view(template_name="AcCitizen/Index.html"),name="Citezen_index"),
    path('citizen_home/', TemplateView.as_view(template_name="AcCitizen/home.html"),name="citizen_home"),
    path('citizen_register/',views.citizen_register,name="citizen_register"),
    path('register_details/',views.Register_Details,name="register_details"),
    path('validation/',views.Validations,name="validations"),
    path('citizen_profile/',views.citizen_profile,name="citizen_profile"),
    path('citizen_logout/',views.Citizen_Logout,name="citizen_logout"),

    path('citizen_Home/', TemplateView.as_view(template_name="AcCitizen/Citizen_Home.html"), name="citizen_Home"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)