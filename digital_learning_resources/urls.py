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
      description='''
      This project aims to provide an API management for digital resources.One can create, read (retrieve), update, or delete a resource. 
      You will have a place to write your notes as you go through the material and either mark it as important for future reference.The API endpoints provided below allow you to interact with the digital resources, including creating new resources, retrieving existing ones, updating their content, and deleting them when no longer needed. To use the API, you'll need to authenticate your requests using our JWT authentication in login endpoint implementation.
      Start with registration endpoint and confirm your email before loggin in.
      ''',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('', include('authentication.urls')),
    path('', include('resources.urls')),
    path('', include('notifications.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
