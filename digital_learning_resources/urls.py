from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Digital Learning Resources Management API",
      default_version='v1',
      description="This project aims to provide an API managment for digital resources. One can create, read(retrieve), update, or delete a resource. You will have a place to write your notes as you go through the material and either mark it as important for future reference",
      terms_of_service="https://www.myapp.com/policies/terms/",
      contact=openapi.Contact(email="contact@digilearn.local"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('', include('authentication.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
