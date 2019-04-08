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

from AcAdmin import views
from ActiveCity import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/",TemplateView.as_view(template_name="AcAdmin/Index.html"),name="Admin_index"),
    path("admin_home/",TemplateView.as_view(template_name="AcAdmin/home.html"),name="admin_home"),
    path("admin_menu/",TemplateView.as_view(template_name="AcAdmin/admin_home.html"),name="admin_menu"),
    path("officer/",views.AddOfficer,name="officer"),
    path("department/",views.departmentHome,name="department"),
    path("dep_delete/",views.Dep_delete,name="dep_delete"),
    path("dep_update/",views.Dep_update,name="dep_update"),
    path("update_departmnet/",views.Update_Departmnet,name="update_departmnet"),





    path("Admindepartment/",views.DepartmentDetails,name="Admindepartment"),
    path("officerRegistaration/",views.OfficerRegistaration,name="officerRegistaration"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)