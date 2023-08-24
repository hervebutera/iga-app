from rest_framework import serializers
from course.models import Course, Course_video

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields = ['title', 'description', 'course_thumbnail']
        

class CourseVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course_video
        fields = ['video']

    def __init__(self, *args, **kwargs):
        self.course = kwargs.pop('course', None)
        super().__init__(*args, **kwargs)
        
    def create(self, validated_data):
        validated_data['course'] = self.course
        return super().create(validated_data)    

