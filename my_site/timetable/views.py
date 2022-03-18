import requests
from django.shortcuts import render, get_object_or_404
from bs4 import BeautifulSoup
from django.views.generic import DetailView

from main.models import CustomUser


def show_timetable(request, group):
    user = CustomUser.objects.filter(group=group).first()
    # group = "АБС-823"
    group = user.group
    url = 'https://www.nstu.ru/studies/schedule/schedule_classes/schedule?group=%s' % group

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    rows = soup.find_all('div', class_='schedule__table-item')
    data = []
    for row in rows:
        temp = row.text

        if (temp.find("&nbsp") < 0):
            data.append(temp)

    return render(request, 'timetable/index.html', {'data': data})
