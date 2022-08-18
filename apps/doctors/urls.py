from django.urls import path

from .views import DoctorListCreateView, DoctorRetrieveUpdateDestroy

urlpatterns = [
    path('',DoctorListCreateView.as_view()),
    path('/<int:pk>',DoctorRetrieveUpdateDestroy.as_view()),
]
