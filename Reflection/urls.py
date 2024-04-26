from django.contrib import admin
from django.urls import path
from .views import HomeView, journal_list, JournalCreateView,  Journal_details, JournalUpdateView, JournalDeleteView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', journal_list, name='journal-list'),
    path('dashboard/journal/create',
         JournalCreateView.as_view(), name='journal-create'),
    path('dashboard/journal/<int:id>/', Journal_details, name='journal-details'),
    path('dashboard/journal/<int:pk>/update',
         JournalUpdateView.as_view(), name='journal-update'),
    path('dashboard/journal/<int:pk>/delete',
         JournalDeleteView.as_view(), name='journal-delete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
