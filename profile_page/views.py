
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.views.generic import *
from gl.utils import *

menu = [
        {'title': 'Создать событие', 'url_name': 'add_event'},
        {'title': 'Создать заметку', 'url_name': 'add_note'},
        {'title': 'Создать группу', 'url_name': 'add_group'},
        {'title': 'О сайте', 'url_name': 'about'},
        ]


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return context | c_def

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Вход')
        return context | c_def

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('login')


class AddProfile(DataMixin, UpdateView):
    template_name = 'add_profile.html'

    def dispatch(self, request, *args, **kwargs):
        form = AddProfileForm(instance=self.get_profile(request.user.profile))
        if request.method == 'POST':
            form = AddProfileForm(request.POST, request.FILES, instance=self.get_profile(request.user.profile))
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                return redirect(reverse("profile"))
        return render(request, self.template_name, {'form': form, 'menu': menu, 'title': 'Редактировать профиль'})

    def get_profile(self, user):
        try:
            return user.profile
        except:
            return None


class ProfileUpdateView(DataMixin, UpdateView):
    model = Profile
    template_name = 'edit_profile.html'
    fields = ['avatar', 'bio', 'city', 'birth_date', 'gender', 'relationship']
    success_url = reverse_lazy('profile')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Редактировать заметку')
        return context | c_def

@login_required
def personal(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    template = "profile.html"
    return render(request, template, context={'menu': menu, 'profile': profile, 'title': 'Моя страница'})

