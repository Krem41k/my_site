import statistics

from django.shortcuts import render


# def index(request):
#     return render(request, 'rating/index.html')
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView

from main.models import CustomUser
from .models import Rating


class TeacherListView(ListView):
    model = Rating
    template_name = 'rating/index.html'
    context_object_name = 'teachers'
    avg_grades = {}
    peoples = CustomUser.objects.all()
    temp = []
    for p in peoples:
        temp.clear()
        grades = p.rating_set.all()
        print(grades)
        for g in grades:
            temp.append(g.grade)
        if len(temp) > 0:
            avg_grades[p.username] = statistics.fmean(temp)
            print(avg_grades)
            print(f"ваша средняя оценка: {statistics.fmean(temp)}")

    extra_context = {'teacher_grade': avg_grades.items()}

    def get_queryset(self):
        # peoples = CustomUser.objects.filter()
        # temp = []
        # for p in peoples:
        #     temp.clear()
        #     grades = p.rating_set.all()
        #     print(grades)
        #     for g in grades:
        #         temp.append(g.grade)
        #     if len(temp) > 0:
        #         print(f"ваша средняя оценка: {statistics.fmean(temp)}")

        # return Rating.objects.filter(user__is_teacher=True)
        return CustomUser.objects.all()

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(TeacherListView, self).get_context_data(**kwargs)
    #     context['avg_grade'] = self.rating_set.all()
    #     return context


class RatingCreateView(CreateView):
    model = Rating
    template_name = 'rating/create_rating.html'
    fields = ['grade', 'comment', 'user']
    success_url = reverse_lazy('rating')
