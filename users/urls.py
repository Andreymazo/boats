from django.contrib.auth.views import LogoutView, PasswordResetConfirmView
from django.urls import path

from users.apps import UsersConfig
from users.views import SigninView, SignupView, SignupSuccessView, verify_email, \
    UserProfileView, CustomPasswordResetView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView, \
    CustomPasswordResetDoneView, simple_reset_password

app_name = UsersConfig.name

urlpatterns = [
    path('', SigninView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignupView.as_view(), name='register'),
    path('register/success/', SignupSuccessView.as_view(), name='register_success'),
    path('password/reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password/reset/<uidb64>/confirm/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password/reset/complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('verify/<str:token>/', verify_email, name='verify_email'),

    path('simple/reset/', simple_reset_password, name='simple_reset'),

    path('profile/', UserProfileView.as_view(), name='profile')
]
