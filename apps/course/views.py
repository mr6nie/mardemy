from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Course
from .serializers import CourseSerializer, CoursesSerializer


class CoursesView(generics.ListAPIView):

    serializer_class = CoursesSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Course.objects.all().order_by("-created")


class CourseView(APIView):
    def get(self, request, course_uuid):

        property = Course.objects.get(course_uuid=course_uuid)
        serializer = CourseSerializer(property, context={"request": request})

        return Response(serializer.data)
