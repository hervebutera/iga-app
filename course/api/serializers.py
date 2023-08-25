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


class CourseVideoWithUrlSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = Course_video
        fields = ['video_url']

    def get_video_url(self, obj):
        return obj.video.url

class CourseWithVideoSerializer(serializers.ModelSerializer):
    course_thumbnail = serializers.SerializerMethodField()
    course_video = CourseVideoWithUrlSerializer(many=True, source='course_video_set')

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'creator', 'course_thumbnail', 'course_video']

    def get_course_thumbnail(self, obj):
        if obj.course_thumbnail:
            return obj.course_thumbnail.url
        return None    
