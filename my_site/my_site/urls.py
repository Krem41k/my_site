from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('timetable/', include('timetable.urls')),
    path('rating/', include('rating.urls')),
]
