from django.db import models
from django.contrib.auth.models import User


class CourseCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="category/")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Course Categories"

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="course/")
    category = models.ForeignKey(
        CourseCategory, related_name="courses", on_delete=models.CASCADE
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category.name} - {self.name}"


class CourseSession(models.Model):
    course = models.ForeignKey(Course, related_name="sessions", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    video = models.FileField(upload_to="video/%Y/%m/%d/")
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.name} - {self.name}"


class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.course.name}"
