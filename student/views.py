from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from base_applicant.views import ApplicationCreateView, ApplicationUpdateView, ApplicationDeleteView, \
    base_submit_application, base_confirm_submit_application, base_view_applications, ApplicationDetailView
from student.models import ScholarshipApplication


class ScholarshipApplicationCreateView(ApplicationCreateView):
    model = ScholarshipApplication
    fields = ApplicationCreateView.fields + ['high_school',
                                             'statement',
                                             'transcript',
                                             'recommendation_letter_1', 'recommendation_letter_2',
                                             'acknowledged']
    template_name = "student/application_form.html"


class ScholarshipApplicationUpdateView(ApplicationUpdateView):
    model = ScholarshipApplication
    fields = ApplicationUpdateView.fields + ['high_school',
                                             'statement',
                                             'transcript',
                                             'recommendation_letter_1', 'recommendation_letter_2',
                                             'acknowledged']
    template_name = "student/application_form.html"


class ScholarshipApplicationDeleteView(ApplicationDeleteView):
    model = ScholarshipApplication
    success_url = reverse_lazy('student:view-apps')  # goes here after confirmation
    template_name = "student/application_confirm_delete.html"  # confirmation page


def home(request):
    """View for the student homepage."""
    return render(request, "student/student_home.html", {'user': request.user})


class ScholarshipApplicationDetailView(ApplicationDetailView):
    model = ScholarshipApplication
    template_name = "student/application_detail.html"


def view_applications(request):
    """View for students to see all of their applications, in a read-only format."""
    return base_view_applications(request,
                                  application_class=ScholarshipApplication,
                                  template_name="student/applications_list.html")


def confirm_submit_application(request, pk: int):
    """Confirmation page before submitting an application."""
    return base_confirm_submit_application(request, pk=pk,
                                           application_class=ScholarshipApplication,
                                           template_name="student/application_confirm_submit.html")


def submit_application(request, pk: int):
    return base_submit_application(request, pk=pk,
                                   application_class=ScholarshipApplication,
                                   success_url=reverse("student:view-apps"))
