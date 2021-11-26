from django.template.defaulttags import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('templates/', views.templates, name='templates'),
    path('note/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='delete_note'),
    path('note/<int:pk>/edit/', views.NoteUpdateView.as_view(), name='edit_note'),
    path('note/new/', views.NoteCreateView.as_view(), name='add_note'),
    path('note/', views.NoteListView.as_view(), name='note'),
    path('event/<int:pk>/delete/', views.EventDeleteView.as_view(), name='delete_event'),
    path('event/<int:pk>/edit/', views.EventUpdateView.as_view(), name='edit_event'),
    path('event/new/', views.EventCreateView.as_view(), name='add_event'),
    path('event/', views.EventListView.as_view(), name='event'),
    path('group/<int:pk>/delete/', views.GroupDeleteView.as_view(), name='delete_group'),
    path('group/<int:pk>/edit/', views.GroupUpdateView.as_view(), name='edit_group'),
    path('group/new/', views.GroupCreateView.as_view(), name='add_group'),
    path('group/', views.GroupListView.as_view(), name='group'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

