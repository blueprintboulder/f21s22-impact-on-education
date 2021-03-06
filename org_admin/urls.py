from django.urls import path

import application
from application.views import VolunteerApplicationCreateView, CollegeApplicationCreateView
from org_admin import views

# org_admin refers to admins of the Impact on Education organization
#  (as opposed to site admins, i.e. the people that administer the website itself)
app_name = 'org_admin'

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.users, name='users'),
    path('account-created/', views.account_created, name='account-created'),


    path('apps/', views.all_apps, name='all-apps'),
    path('apps/new/', views.create_application, name='new-app'),

    path('apps/scholarship/', views.all_scholarship_apps, name='all-scholarship-apps'),
    path('apps/scholarship/new', views.ScholarshipApplicationCreateView.as_view(), name='new-scholarship-app'),
    path('apps/scholarship/<int:pk>/', views.ScholarshipApplicationDetailView.as_view(), name='view-scholarship-app'),
    path('apps/scholarship/<int:pk>/confirm-delete/', views.ScholarshipApplicationDeleteView.as_view(),
         name='confirm-delete-scholarship-app'),

    path('apps/academic-funding/', views.all_academic_funding_apps, name='all-academic-funding-apps'),
    path('apps/academic-funding/new', views.AcademicFundingApplicationCreateView.as_view(),
         name='new-academic-funding-app'),
    path('apps/academic-funding/<int:pk>/', views.AcademicFundingApplicationDetailView.as_view(),
         name='view-academic-funding-app'),
    path('apps/academic-funding/<int:pk>/confirm-delete/', views.AcademicFundingApplicationDeleteView.as_view(),
         name='confirm-delete-academic-funding-app'),
    path('apps/volunteer-app/new', VolunteerApplicationCreateView.as_view(),
             name='new-volunteer-app'),
    # path('apps/volunteer-app/<int:pk>/', views.VolunteerApplicationDetailView.as_view(),
    #      name='view-volunteer-app'),
    # path('apps/volunteer-app/<int:pk>/confirm-delete/', views.VolunteerApplicationDeleteView.as_view(),
    #      name='confirm-delete-volunteer-app'),
    path('apps/college-app/new', CollegeApplicationCreateView.as_view(),
             name='new-college-app'),
#     path('apps/college-app/<int:pk>/', views.CollegeApplicationDetailView.as_view(),
#          name='view-college-app'),
    # path('apps/college-app/<int:pk>/confirm-delete/', views.CollegeApplicationDeleteView.as_view(),
    #      name='confirm-delete-college-app'),
]
