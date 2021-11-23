from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from .models import *


class AddEventForm(forms.ModelForm):


    class Meta:
        model = Events
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длинна превышает 200 символов')
        return title


class AddNoteForm(forms.ModelForm):

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title

    class Meta:
        model = Notes
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }


class AddGroupForm(forms.ModelForm):

    class Meta:
        model = Groups
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title