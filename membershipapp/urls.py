from django.urls import path

from membershipapp.views import UserSignUpView, UpdateProfileView, ProfileDetailView

urlpatterns=[
    path('register/', UserSignUpView.as_view(), name='register'),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/update_profile/<int:pk>',UpdateProfileView.as_view(), name='update-profile'),
]