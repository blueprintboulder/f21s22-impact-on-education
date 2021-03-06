from django.urls import path

from student import views
from student.views import ScholarshipApplicationCreateView, ScholarshipApplicationUpdateView,\
    ScholarshipApplicationDeleteView, AcademicFundingApplicationCreateView

app_name = 'scholarship'
urlpatterns = [
    path('', views.home, name='home'),
    path('apps/', views.my_applications, name='view-apps'),
    path('apps/new/', ScholarshipApplicationCreateView.as_view(), name='new-app'),
    path('apps/<int:pk>/', views.ScholarshipApplicationDetailView.as_view(), name='view-app'),
    path('apps/<int:pk>/edit/', ScholarshipApplicationUpdateView.as_view(), name='edit-app'),
    path('apps/<int:pk>/confirm-delete/', ScholarshipApplicationDeleteView.as_view(), name='confirm-delete-app'),
    path('apps/<int:pk>/confirm-submit/', views.confirm_submit_application, name='confirm-submit-app'),
    path('apps/<int:pk>/submit/', views.submit_application, name='submit-app'),
    path('profile/', views.profile, name='profile'),
    path('apps/academic-funding/', AcademicFundingApplicationCreateView.as_view(), name='academic-funding'),
]
