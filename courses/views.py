from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render 
from .models import Course, Enrollment, CourseCategory


def courses(request):
    courses_categories = CourseCategory.objects.all()
    return render(
        request,
        "courses/courses.html",
        context={"courses_categories": courses_categories},
    )


def category_detail(request, category_id):
    category = CourseCategory.objects.get(id=category_id)
    return render(
        request, "courses/category_detail.html", context={"category": category}
    )


@login_required(login_url="/login")
def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    is_enrolled = Enrollment.objects.filter(
        student=request.user, course=course
    ).exists()
    enrollment = Enrollment.objects.filter(student=request.user, course=course).first()
    return render(
        request,
        "courses/course_detail.html",
        context={
            "course": course,
            "enrollment": enrollment,
            "is_enrolled": is_enrolled,
        },
    )


def course_enroll(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        Enrollment.objects.create(course=course, student=request.user)
    return redirect("courses:course_detail", course_id=course_id)
