import statistics

from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from main.models import CustomUser
from .models import Rating


class TeacherListView(ListView):
    model = Rating
    template_name = 'rating/index.html'
    context_object_name = 'users'
    avg_grades = {}
    peoples = CustomUser.objects.all()
    temp_for_grade = []
    for p in peoples:
        temp_for_grade.clear()
        grades = p.rating_set.all()
        print(grades)
        for g in grades:
            temp_for_grade.append(g.grade)
        if len(temp_for_grade) > 0:
            avg_grades[p.username] = statistics.fmean(temp_for_grade)
            print(avg_grades)

    extra_context = {'user_rating': avg_grades.items()}

    def get_queryset(self):
        return Rating.objects.all()


class RatingCreateView(CreateView):
    model = Rating
    template_name = 'rating/create_rating.html'
    fields = ['grade', 'comment', 'user']
    success_url = reverse_lazy('rating')


# class RatingDetailView(DetailView):
#     model = Rating
#     template_name = 'rating/details_view.html'
#     context_object_name = 'user_rating'

def rating_detail(request, user):
    u = Rating.objects.filter(user__username=user)

    return render(request, 'rating/details_view.html', {'data': u})
