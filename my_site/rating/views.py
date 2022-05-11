from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Avg, Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from main.models import CustomUser

from .forms import RatingForm, RatingDetailForm
from .utils import RatingMixinPassesTest


class RatingListView(ListView):
    queryset = CustomUser.objects.annotate(average_rating=Avg('rating__grade'))
    template_name = 'rating/index.html'
    context_object_name = 'users_avg'

    def get_ordering(self):
        ordering = self.request.GET.get('orderby', '-average_rating')
        return ordering


class RatingCreateView(RatingMixinPassesTest, CreateView):
    form_class = RatingForm
    template_name = 'rating/create_rating.html'
    success_url = reverse_lazy('rating')


def rating_detail(request, user):
    comments = CustomUser.objects.get(username=user).rating_set.all()
    users = CustomUser.objects.annotate(average_rating=Avg('rating__grade')).get(username=user)
    return render(request, 'rating/details_view.html', {'comments': comments, 'users': users})


class DetailRatingCreateView(RatingMixinPassesTest, CreateView):
    form_class = RatingDetailForm
    template_name = 'rating/create_rating.html'
    success_url = reverse_lazy('rating')

    def form_valid(self, form):
        user = CustomUser.objects.get(username=self.kwargs['user'])
        form.instance.user = user
        return super(DetailRatingCreateView, self).form_valid(form)
