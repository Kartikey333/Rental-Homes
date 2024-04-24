from django.urls import path
from . import views
from allauth.account import views as auth_views


urlpatterns = [
    path("house/<int:pk>/", views.house_detail, name="house-detail"),
    path("house/update/<int:pk>/", views.house_update, name="house-update"),
    path("house/<str:user>/", views.house_list, name="house-list"),

    path("", views.room_index, name="room-index"),
    path("room/<int:pk>/", views.room_details, name="room-details"),
    path("room/update/<int:pk>/", views.room_update, name="room-update"),
    path('add/house/',views.add_house, name='add-house'),
    path('add/<int:pk>/room/', views.add_room, name='add-room'),

    path('accounts/login/', views.allauth_login, name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', views.allauth_signup, name='signup'),

    # password reset
    path('accounts/password/reset/', auth_views.PasswordResetView.as_view(), name='account_reset_password'),
    # Change password
    path('accounts/password/change/', auth_views.PasswordChangeView.as_view(), name='account_change_password'),

    path('email/', auth_views.EmailView.as_view(), name='account_email'),
    path('email/sent/', auth_views.EmailVerificationSentView.as_view(), name='account_email_verification_sent'),
    path('confirm-email/', auth_views.ConfirmEmailView.as_view(), name='account_confirm_email'),
    
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    # path('signup/', views.signup_view, name='signup'),

]
