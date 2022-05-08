from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

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
            Q(title__icontains=query) | Q(user__username__icontains=query) | Q(pk__icontains=query)
        )
        return object_list


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/course_edit.html'
    fields = '__all__'

    def get_success_url(self, **kwargs):
        return reverse_lazy('detail_course', kwargs={'pk': self.kwargs['pk']})


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/course_delete.html'
    success_url = reverse_lazy('courses')


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


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'lessons/detail_lesson.html'


class LessonUpdateView(UpdateView):
    model = Lesson
    template_name = 'lessons/lesson_edit.html'
    fields = '__all__'

    def get_success_url(self, **kwargs):
        return reverse_lazy('detail_lesson', kwargs={'pk': self.kwargs['pk']})


class LessonDeleteView(DeleteView):
    model = Lesson
    template_name = 'lessons/lesson_delete.html'

    def get_success_url(self, **kwargs):
        pk_course = Lesson.objects.get(id=self.kwargs['pk']).course.id
        return reverse_lazy('detail_course', kwargs={'pk': pk_course})
