from django.contrib import admin
from django.utils.html import format_html
from .models import Course, CourseCategory, Enrollment, CourseSession


class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at")
    search_fields = ("name", "description")
    list_filter = ("created_at",)


class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "description", "created_at")
    search_fields = ("name", "description")
    list_filter = ("created_at", "category__name")


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("course", "student", "enrolled_at")
    search_fields = ("course__name", "student__username")
    list_filter = ("enrolled_at", "course__name")


class CourseSessionAdmin(admin.ModelAdmin):
    list_display = ("course", "name", "video_link", "create_at")
    search_fields = ("course__name", "name")
    list_filter = ("create_at",)

    def video_link(self, obj):
        return format_html(
            '<a href="{}" target="_blank">{}</a>'.format(obj.video.url, obj.name)
        )



admin.site.register(CourseCategory, CourseCategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(CourseSession, CourseSessionAdmin)

