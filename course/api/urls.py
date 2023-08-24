from django.urls import path
from course.api.views import (
    api_create_course_view
)

app_name = 'course'

urlpatterns = [
    path('upload', api_create_course_view, name='upload_course')
    # /course/upload  API for uploading a new course
]

