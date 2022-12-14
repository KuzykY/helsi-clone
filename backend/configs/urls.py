from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view

from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Helsi_clone API",
        default_version='v1',
        description="About",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)
urlpatterns = [
    path('auth', include('apps.auth.urls')),
    path('users', include('apps.users.urls')),
    path('doctors', include('apps.doctors.urls')),
    path('patients', include('apps.patients.urls')),
    path('medical_cards', include('apps.medical_cards.urls')),
    path('doc',schema_view.with_ui('swagger',cache_timeout=0)),
]

# handler500 = 'rest_framework.exceptions.server_error'
# handler400 = 'rest_framework.exceptions.bad_request'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
