from django.urls import path

from users.apps import UsersConfig
from users.views import UserRegister, UserListAPIView, UserAuthorizationView, PasswordRecoveryView, \
    RequestPasswordRecoveryView, UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListAPIView.as_view(), name='users'),
    path('sign-up/', UserRegister.as_view(), name='user_register'),
    path('sign-in/', UserAuthorizationView.as_view(), name='user_authorization'),
    path('<int:pk>/delete/', UserDestroyAPIView.as_view(), name='user_delete'),

    path('recovery/', RequestPasswordRecoveryView.as_view(), name='password_recovery'),
    path('recovery/<str:hash>/', PasswordRecoveryView.as_view(), name='password_recovery'),
]
