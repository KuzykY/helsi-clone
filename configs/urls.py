from django.urls import include, path
from django.conf.urls.static import static

from configs import settings

urlpatterns = [
    path('auth', include('apps.auth.urls')),
    path('users', include('apps.users.urls')),
    path('doctors', include('apps.doctors.urls')),
    path('patients', include('apps.patients.urls')),
    path('medical_cards', include('apps.medical_cards.urls')),
]

# handler500 = 'rest_framework.exceptions.server_error'
# handler400 = 'rest_framework.exceptions.bad_request'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
