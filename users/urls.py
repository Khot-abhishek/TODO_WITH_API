from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registration, name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),

#     path('pasword-reset/', views.PResetView.as_view(), name='pasword_reset'),
#     path('password-reset/done/', views.PResetDoneView.as_view(), name='password_reset_done'),
#     path('password-reset-confirm/<uidb64>/<token>/', views.PResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('password-reset-complete/', views.PResetCompleteView.as_view(), name='password_reset_complete'),
]