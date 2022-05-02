from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Course, Lesson


class CourseListView(ListView):
    model = Course
    template_name = 'courses/index.html'
    context_object_name = 'courses'

    # def get_ordering(self):
    #     ordering = self.request.GET.get('orderby', 'title')
    #     return ordering


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/create_course.html'
    success_url = reverse_lazy('courses')
    fields = '__all__'


def course_detail(request, pk):
    course = Course.objects.get(id=pk)
    lessons = course.lesson_set.all()
    return render(request, 'courses/detail_course.html', {'course': course, 'lessons': lessons})


class SearchResultsView(ListView):
    model = Course
    template_name = 'courses/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Course.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(user__username__icontains=query)
        )
        return object_list


class LessonCreateView(CreateView):
    model = Lesson
    template_name = 'lessons/create_lesson.html'
    success_url = reverse_lazy('courses')
    fields = '__all__'
