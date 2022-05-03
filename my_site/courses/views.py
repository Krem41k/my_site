from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Course, Lesson


class CourseListView(ListView):
    model = Course
    template_name = 'courses/index.html'
    context_object_name = 'courses'

    def get_ordering(self):
        ordering = self.request.GET.get('orderby', 'title')
        return ordering


class CourseCreateView(UserPassesTestMixin, CreateView):
    model = Course
    template_name = 'courses/create_course.html'
    success_url = reverse_lazy('courses')
    fields = '__all__'

    def get_initial(self, *args, **kwargs):
        initial = super(CourseCreateView, self).get_initial(**kwargs)
        initial['user'] = self.request.user.pk
        return initial

    def test_func(self):
        return self.request.user.is_teacher

    def handle_no_permission(self):
        return redirect('courses')


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
            Q(title__icontains=query) | Q(description__icontains=query)
            | Q(user__username__icontains=query) | Q(pk__icontains=query)
        )
        return object_list


class LessonCreateView(UserPassesTestMixin, CreateView):
    model = Lesson
    template_name = 'lessons/create_lesson.html'
    success_url = reverse_lazy('courses')
    fields = '__all__'

    def get_initial(self, *args, **kwargs):
        initial = super(LessonCreateView, self).get_initial(**kwargs)
        initial['course'] = Course.objects.get(id=self.kwargs['pk'])
        return initial

    def test_func(self):
        return self.request.user.is_teacher

    def handle_no_permission(self):
        return redirect('courses')
