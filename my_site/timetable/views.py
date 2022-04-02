import requests
from django.shortcuts import render
from bs4 import BeautifulSoup


def show_timetable(request, user_group):
    url = 'https://www.nstu.ru/studies/schedule/schedule_classes/schedule?group=%s' % user_group

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    rows = soup.find_all('div', class_='schedule__table-item')
    data = []
    for row in rows:
        temp = row.text

        if temp.find("&nbsp") < 0:
            data.append(temp)

    return render(request, 'timetable/index.html', {'data': data})
