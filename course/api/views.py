from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from course.models import Course, Category, Course_video
from course.api.serializers import CourseSerializer, CourseVideoSerializer, CourseWithVideoSerializer


def save_course_video(request, course):
    course_data = Course_video(course=course)
    video_serialised = CourseVideoSerializer(course_data, data=request.data)

    if video_serialised.is_valid():
        video_serialised.save()
    else:    
        return Response(video_serialised.errors, status=status.HTTP_400_BAD_REQUEST)  


@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def api_create_course_view(request):
    account = request.user
    category_selected = Category.objects.get(name=request.data['category'])

    course = Course(creator=account, 
                    category=category_selected,
                    )

    course_serialised = CourseSerializer(course, data=request.data)
    saved_course = ""
    if course_serialised.is_valid():
        saved_course = course_serialised.save()
    else:
        return Response(course_serialised.errors, status=status.HTTP_400_BAD_REQUEST)    

    try:
        course = Course.objects.get(title=saved_course.title)
    except Course.DoesNotExist:
        return Response({
            'error': 'There has been a problem trying to upload the course. Try again later.'
            }, status=status.HTTP_404_NOT_FOUND)

    save_course_video(request, course)   

    data = {}
    data['response'] = f"Course with title: {request.data['title']} has been uploaded successfully."

    return Response(data, status = status.HTTP_201_CREATED) 


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def api_all_courses_with_videos_view(request):
    courses = Course.objects.all()
    serializer = CourseWithVideoSerializer(courses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def api_single_course_with_video_view(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CourseWithVideoSerializer(course)
    return Response(serializer.data, status=status.HTTP_200_OK)

