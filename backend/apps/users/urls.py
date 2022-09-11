from django.urls import path

from apps.users.views import (
    AddAvatarView,
    DoctorToUserView,
    UserListCreateView,
    UserRetrieveUpdateDestroyView,
    UserToDoctorView,
)

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/avatars', AddAvatarView.as_view()),
    path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view()),
    path('/<int:pk>/doctor', UserToDoctorView.as_view()),
    path('/<int:pk>/not_doctor', DoctorToUserView.as_view()),
]
