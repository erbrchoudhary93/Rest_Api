from django.urls import  re_path

from .import views
from django.conf.urls.static import static
from django.conf import settings




urlpatterns =[
            re_path(r'^department$',views.departmentapi),  # for GET ,POST ,PUT request
            re_path(r'^department/([0-9]+)$',views.departmentapi),  # for DELETE request
            
            re_path(r'^employee$',views.employeeapi),     # for GET ,POST ,PUT request
            re_path(r'^employee/([0-9]+)$',views.employeeapi), # for DELETE request
            
            re_path(r'^employee/savefile',views.savefile)    # for file saving
            
            
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)