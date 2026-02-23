from django.urls import path

from . import views


app_name = "shop"

urlpatterns = [
    # Main shop page showing all courses
    path("", views.index, name="index"),
    # Single course detail page with integer ID parameter validation
    path("<int:course_id>/", views.single_course, name="single_course"),
]
