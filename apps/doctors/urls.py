from django.urls import path

from .views import DoctorListCreateView, DoctorRetrieveDestroyView

urlpatterns = [
    path('', DoctorListCreateView.as_view()),
    path('/<int:pk>', DoctorRetrieveDestroyView.as_view()),
]
