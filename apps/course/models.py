import uuid

from django.db import models
from django.contrib.auth import get_user_model

from cloudinary_storage.storage import MediaCloudinaryStorage
from cloudinary.models import CloudinaryField


User = get_user_model()


class Course(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    student_rating = models.IntegerField(default=0)
    language = models.CharField(max_length=225)
    course_length = models.CharField(default=0, max_length=20)
    course_sections = models.ManyToManyField("CourseSection", blank=True)
    course_uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    image_url = models.ImageField(
        upload_to="course_images", storage=MediaCloudinaryStorage()
    )
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title


class CourseSection(models.Model):
    section_title = models.CharField(max_length=225, blank=True, null=True)
    section_number = models.IntegerField(blank=True, null=True)
    episodes = models.ManyToManyField("Episode", blank=True)

    class Meta:
        verbose_name = "Секция"
        verbose_name_plural = "Секции"

    def __str__(self):
        return self.section_title


class Episode(models.Model):
    title = models.CharField(max_length=225)
    file = CloudinaryField(resource_type="video", folder="media")
    length = models.DecimalField(max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = "Эпизод"
        verbose_name_plural = "Эпизоды"

    def __str__(self):
        return self.title
