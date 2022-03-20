from django.contrib.auth import get_user_model

from decimal import Decimal

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .helpers import get_timer

from .models import CourseSection, Episode, Course


class CoursesSerializer(ModelSerializer):
    brief_description = serializers.SerializerMethodField(read_only=True)
    author = serializers.CharField(source="author.username")
    created = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Course
        fields = [
            "course_uuid",
            "title",
            "brief_description",
            "created",
            "author",
            "language",
            "image_url",
            "price",
        ]

    def get_brief_description(self, obj):
        return obj.description[:100]


class EpisodePaidSerializer(ModelSerializer):
    length = serializers.SerializerMethodField(read_only=True)
    file = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Episode
        fields = [
            "title",
            "file",
            "length",
        ]

    def get_length(self, obj):
        video = obj.length
        return get_timer(video)

    def get_file(self, obj):
        return obj.file.url


class CourseSectionSerializer(ModelSerializer):
    episodes = EpisodePaidSerializer(many=True, read_only=True)
    total_length = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CourseSection
        fields = [
            "section_title",
            "section_number",
            "total_length",
            "episodes",
        ]

    def get_total_length(self, obj):
        total = Decimal(0.00)
        for episode in obj.episodes.all():
            total += episode.length
        return get_timer(total, type="short")


class CourseSerializer(ModelSerializer):
    course_sections = CourseSectionSerializer(many=True, read_only=True)
    brief_description = serializers.SerializerMethodField(read_only=True)
    author = serializers.CharField(source="author.username")
    created = serializers.DateTimeField(format="%Y-%m-%d")
    updated = serializers.DateTimeField(format="%Y-%m-%d")
    total_lectures = serializers.SerializerMethodField(read_only=True)
    total_course_length = serializers.SerializerMethodField(read_only=True)
    enrolled_students = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = [
            "course_uuid",
            "title",
            "description",
            "brief_description",
            "created",
            "updated",
            "author",
            "enrolled_students",
            "total_lectures",
            "total_course_length",
            "student_rating",
            "language",
            "course_length",
            "course_sections",
            "image_url",
            "price",
        ]

    def get_enrolled_students(self, obj):
        students = get_user_model().objects.all()
        # filter(paid_course=self)
        return len(students)

    def get_brief_description(self, obj):
        return obj.description[:150]

    def get_total_lectures(self, obj):
        lectures = 0
        for section in obj.course_sections.all():
            lectures += len(section.episodes.all())
        return lectures

    def get_total_course_length(self, obj):
        length = Decimal(0.00)

        for section in obj.course_sections.all():
            for episode in section.episodes.all():
                length += episode.length

        return get_timer(length, type="short")
