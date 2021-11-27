from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy

from profile_page.models import Profile
from .forms import *
from .models import *
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .utils import *

menu = [
        {'title': 'Создать событие', 'url_name': 'add_event'},
        {'title': 'Создать заметку', 'url_name': 'add_note'},
        {'title': 'Создать группу', 'url_name': 'add_group'},
        {'title': 'О сайте', 'url_name': 'about'},
        ]


def home(request):
    context = {'menu': menu, 'title': 'Главная'}
    return render(request, 'index.html', context=context)


def templates(request):
    context = {'menu': menu, 'title': 'Шаблоны'}
    return render(request, 'templates.html', context=context)


def about(request):
    context = {'menu': menu, 'title': 'О сайте'}
    return render(request, 'about.html', context=context)


class NoteListView(DataMixin, ListView):
    model = Notes
    template_name = 'notes.html'

    def get_queryset(self, *args, **kwargs):
        return Notes.objects.filter(person=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Заметки')
        return context | c_def


class NoteCreateView(DataMixin, CreateView):  # новое изменение
    model = Notes
    form = AddNoteForm()
    template_name = 'add_note.html'
    fields = ['title', 'description', 'date', 'person', 'done']
    success_url = reverse_lazy('note')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Создать заметку')
        return context | c_def


class NoteUpdateView(DataMixin, UpdateView):
    model = Notes
    template_name = 'edit_note.html'
    fields = ['title', 'description', 'date', 'done']
    success_url = reverse_lazy('note')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Редактировать заметку')
        return context | c_def


class NoteDeleteView(DataMixin, DeleteView):
    model = Notes
    template_name = 'delete_note.html'
    success_url = reverse_lazy('note')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Редактировать заметку')
        return context | c_def


class EventListView(DataMixin, ListView):
    model = Events
    template_name = 'events.html'

    def get_queryset(self):
        group = Groups.objects.filter(persons=self.request.user)
        events_g = Events.objects.filter(groups__in=group)
        events = Events.objects.filter(person=self.request.user)
        return events | events_g

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='События')
        return context | c_def


class EventCreateView(DataMixin, CreateView):  # новое изменение
    model = Events
    form = AddEventForm()
    template_name = 'add_event.html'
    fields = ['title', 'groups', 'date', 'person', 'done']
    success_url = reverse_lazy('event')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Создать событие')
        return context | c_def


class EventUpdateView(DataMixin, UpdateView):
    model = Events
    template_name = 'edit_event.html'
    fields = ['title', 'groups', 'date', 'person', 'done']
    success_url = reverse_lazy('event')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Редактировать обытие')
        return context | c_def


class EventDeleteView(DataMixin, DeleteView):
    model = Events
    template_name = 'delete_event.html'
    success_url = reverse_lazy('event')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Удалить событие')
        return context | c_def


class GroupListView(DataMixin, ListView):
    model = Groups
    template_name = 'groups.html'

    def get_queryset(self, *args, **kwargs):
        persons = Profile.objects.all()
        return Groups.objects.filter(persons=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Группы')
        return context | c_def


class GroupCreateView(DataMixin, CreateView):
    model = Groups
    form = AddGroupForm()
    template_name = 'add_group.html'
    fields = ['title', 'photo', 'persons']
    success_url = reverse_lazy('group')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Создать группу')
        return context | c_def


class GroupUpdateView(DataMixin, UpdateView):
    model = Groups
    template_name = 'edit_group.html'
    fields = ['title', 'photo', 'persons']
    success_url = reverse_lazy('group')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Редактировать группу')
        return context | c_def


class GroupDeleteView(DataMixin, DeleteView):
    model = Groups
    template_name = 'delete_group.html'
    success_url = reverse_lazy('group')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Удалить группу')
        return context | c_def
