from django.urls import path
from accounts import views

app_name = "accounts"
urlpatterns = [
    # Most URLs here are copied from the URLs in django.contrib.auth.urls, with slight changes
    #  (e.g. the URLs here separated by dashes instead of underscores)
    #  Django's documentation for django.contrib.auth.urls:
    #  https://docs.djangoproject.com/en/3.2/topics/auth/default/#module-django.contrib.auth.views
    #  The URLs 'register/' and 'account-created/' are not copied from there.

    path('login/', views.LoginView.as_view(), name='login'),

    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.ProfileEditView.as_view(), name='profile-edit'),
    path('profile/saved', views.profile_saved, name='profile-saved'),

    path('password-change/', views.PasswordChangeView.as_view(), name='password-change'),
    path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password-change-done'),

    path('password-reset/', views.PasswordResetView.as_view(), name='password-reset'),
    path('password-reset/email-sent', views.PasswordResetEmailSentView.as_view(), name='password-reset-email-sent'),
    path('reset/<uidb64>/<token>/', views.PasswordResetEnterNewPasswordView.as_view(),
         name='password-reset-enter-new-password'),
    path('reset/done', views.PasswordResetCompleteView.as_view(), name='password-reset-complete'),

    path('register/', views.CustomUserCreateView.as_view(), name='register'),
    path('account-created/', views.account_created, name='account-created'),

    # TODO (low priority): Move the homepage-redirect URL from django_root to here (along with its view)
]
