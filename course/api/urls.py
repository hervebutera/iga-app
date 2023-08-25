from django.urls import path
from course.api.views import (
    api_create_course_view,
    api_all_courses_with_videos_view,
    api_single_course_with_video_view
)

app_name = 'course'

urlpatterns = [
    path('upload', api_create_course_view, name='upload_course'),
    # /course/upload  API for uploading a new course

    path('view-all', api_all_courses_with_videos_view, name='all-courses-with-videos'),
    # /course/view-all  API for viewing all courses

    path('detail/<int:course_id>/', api_single_course_with_video_view, name='single-course-with-video'),
    # /course/detail/<int:course_id>  API for viewing a single course
]

