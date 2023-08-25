from django.conf import settings
from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
         verbose_name = 'Category'
         verbose_name_plural = 'Categories'


    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False, unique=True)
    description = models.TextField(blank = True, null = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course_thumbnail = models.FileField(upload_to='iga-app-course-thumbnails', null=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Course_video(models.Model):
    video = CloudinaryField(resource_type='video', folder='iga-app-course-videos', null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Enrollments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=60)

