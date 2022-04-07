from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('timetable/', include('timetable.urls')),
    path('rating/', include('rating.urls')),
    path('library/', include('library.urls')),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
