from django.urls import include, path

urlpatterns = [
    path('users', include('apps.users.urls')),
    path('doctors', include('apps.doctors.urls')),
    path('patients', include('apps.patients.urls')),
    path('medical_cards', include('apps.medical_cards.urls')),
]
