from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.urls import reverse


class Groups(models.Model):
    title = models.CharField(max_length=150,null=True, verbose_name='Название')
    photo = models.ImageField(verbose_name=u"Аватар", null=True, blank=True, upload_to='avatar/%Y/%m/%d/')
    persons = models.ManyToManyField(User, related_name='persons')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('group', kwargs={'group_id': self.pk})


class Events(models.Model):
    title = models.CharField(max_length=150, verbose_name='Событие')
    date = models.DateField('Дата события')
    groups = models.ManyToManyField('Groups', blank=True, verbose_name='Группы')
    done = models.BooleanField(default=False, verbose_name='Выполнено')
    person = models.ManyToManyField(User, related_name='person', blank=True, verbose_name='Участники')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('event', kwargs={'event_id': self.pk})


class Notes(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название заметки')
    description = models.TextField(verbose_name='Заметки', blank=True)
    date = models.DateTimeField('Дата', blank=True, null=True)
    person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    done = models.BooleanField(default=False, verbose_name='Выполнено')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('note', kwargs={'note_id': self.pk})





