from django.urls import path

from .views import AddPatientToDoctorView, DoctorListCreateView, DoctorRetrieveDestroyView

urlpatterns = [
    path('', DoctorListCreateView.as_view()),
    path('/<int:pk>', DoctorRetrieveDestroyView.as_view()),
    path('/<int:pk>/patients', AddPatientToDoctorView.as_view()),
]
