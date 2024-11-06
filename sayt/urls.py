
from django.contrib import admin
from django.conf.urls.static import static
from . import settings
from django.urls import path,include

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from my_app.views import render_site


schema_view = get_schema_view(
   openapi.Info(
      title="FarGenius API Documentation",
      default_version='v1',
      description="sjdfhsjdfhjsdhgbsj",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', render_site),  # Django admin site
    path('ru/', render_site),
    path('en/', render_site),
    path('admin/', admin.site.urls),  # Django admin site
    path('api/', include([
        path('api28/', include('my_app.urls')),  # your API endpoints
        path('payment/', include('pay_me.urls')), # payme uchun
        path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ])),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
