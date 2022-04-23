import requests
from django.shortcuts import render
from bs4 import BeautifulSoup


def show_timetable(request, user_group):
    url = 'https://www.nstu.ru/studies/schedule/schedule_classes/schedule?group=%s' % user_group

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    test = soup.find_all('div', class_='schedule__table-row')
    temp1 = []
    for t in test:
        if t.text.find("&nbsp") < 0:
            temp1.append(t.text)
    # for t in range(0, len(test), 2):
    #     if test[t].text.find("&nbsp") < 0:
    #         temp1.append(test[t].text)
    rows = soup.find_all('div', class_='schedule__table-item')
    table_day = soup.find_all('div', class_='schedule__table-day')
    days = []
    table_time = soup.find_all('div', class_='schedule__table-time')
    times = []

    for time in table_time:
        times.append(time.text)

    for day in table_day:
        days.append(day.text)

    data = []

    for row in rows:
        temp = row.text

        if temp.find("&nbsp") < 0:
            data.append(temp)

    return render(request, 'timetable/index.html', {'data': data, 'days': days, 'times': times, 'temp': temp1})
