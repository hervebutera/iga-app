from django.db import models
from account.models import Account


class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
         verbose_name = 'Category'
         verbose_name_plural = 'Categories'


    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_lenth=300, blank=False, null=False)
    description = models.TextField(blank = True, null = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    creator = models.ForeignKey(Account, on_delete=models.CASCADE)
    course_thumbnail = models.CharField(max_length=500, null=False, blank=False)
    thumbnail_cloudinary_id = models.CharField(max_length=200, null=False, blank=False)

    class meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Course_videos(models.Model):
    video_url = models.CharField(max_length=500, null=False, blank=False)
    video_cloudinary_id = models.CharField(max_length=300, null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Enrollments(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=60, default='enrolled')

