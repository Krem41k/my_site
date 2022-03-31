import statistics

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from main.models import CustomUser
from .models import Rating


def avg():
    avg_grades = {}
    peoples = CustomUser.objects.all()
    temp_for_grade = []
    for p in peoples:
        temp_for_grade.clear()
        grades = p.rating_set.all()
        for g in grades:
            temp_for_grade.append(g.grade)
        if len(temp_for_grade) > 0:
            avg_grades[p.username] = round(statistics.fmean(temp_for_grade), 2)
    return avg_grades


class TeacherListView(ListView):
    model = Rating
    template_name = 'rating/index.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avg_grades'] = avg()
        return context


class RatingCreateView(CreateView):
    model = Rating
    template_name = 'rating/create_rating.html'
    fields = ['grade', 'comment', 'user']
    success_url = reverse_lazy('rating')


def rating_detail(request, user):
    comments = Rating.objects.filter(user__username=user)
    u = CustomUser.objects.filter(username=user).first()
    avg_grade = avg().get(u.username)
    return render(request, 'rating/details_view.html', {'comments': comments, 'avg_grade': avg_grade,
                                                        'username': u.username})
