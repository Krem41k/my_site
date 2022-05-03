import statistics

from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from main.models import CustomUser

from .forms import RatingForm
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
    sorted_avg_grades = dict(sorted(avg_grades.items(), reverse=True, key=lambda item: item[1]))
    return sorted_avg_grades


def rating_list(request):
    return render(request, 'rating/index.html', {'avg_grades': avg()})


class RatingCreateView(UserPassesTestMixin, CreateView):
    form_class = RatingForm
    template_name = 'rating/create_rating.html'
    success_url = reverse_lazy('rating')

    def test_func(self):
        return self.request.user.is_teacher is False

    def handle_no_permission(self):
        return redirect('rating')


def rating_detail(request, user):
    comments = Rating.objects.filter(user__username=user)
    avg_grade = avg().get(user)
    return render(request, 'rating/details_view.html', {'comments': comments, 'avg_grade': avg_grade,
                                                        'username': user})
