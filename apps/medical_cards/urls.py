from django.urls import path

from .views import MedicalCardListCreateView

urlpatterns = [
    path('',MedicalCardListCreateView.as_view()),
    # path('/<int:pk>',.as_view()),
]
