from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import CourseForm, LessonForm
from .models import Course, Lesson


class CourseListView(ListView):
    model = Course
    template_name = 'courses/index.html'
    context_object_name = 'courses'

    def get_ordering(self):
        ordering = self.request.GET.get('orderby', 'title')
        return ordering


class CourseCreateView(UserPassesTestMixin, CreateView):
    form_class = CourseForm
    template_name = 'courses/create_course.html'
    success_url = reverse_lazy('courses')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CourseCreateView, self).form_valid(form)

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
    form_class = LessonForm
    template_name = 'lessons/create_lesson.html'

    def form_valid(self, form):
        course = Course.objects.get(id=self.kwargs['pk'])
        form.instance.course = course
        return super(LessonCreateView, self).form_valid(form)

    def test_func(self):
        return self.request.user.is_teacher

    def handle_no_permission(self):
        return redirect('courses')

    def get_success_url(self, **kwargs):
        return reverse_lazy('detail_course', kwargs={'pk': self.kwargs['pk']})
