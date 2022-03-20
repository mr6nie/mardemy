from django.urls import path
from . import views

urlpatterns = [
    path("", views.CoursesView.as_view(), name="courses"),
    path(
        "<uuid:course_uuid>",
        views.CourseView.as_view(),
        name="course",
    ),
]
