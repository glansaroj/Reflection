from django.contrib import admin
from django.urls import path
from .views import HomeView, journal_list, JournalCreateView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', journal_list, name='journal-list'),
    path('dashboard/journal/create',
         JournalCreateView.as_view(), name='journal-create'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
