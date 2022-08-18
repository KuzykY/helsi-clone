from django.urls import path

from .views import PatientListCreateView, PatientRetrieveUpdateDestroyView

urlpatterns = [
    path('', PatientListCreateView.as_view()),
    path('/<int:pk>',PatientRetrieveUpdateDestroyView.as_view()),
]
