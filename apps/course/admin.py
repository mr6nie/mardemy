from django.contrib import admin

from .models import Course, CourseSection, Episode


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "file", "length"]
    list_display_links = ["id", "title", "file"]


admin.site.register(Episode, EpisodeAdmin)
admin.site.register(CourseSection)


admin.site.register(Course)
