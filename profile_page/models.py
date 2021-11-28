from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.urls import reverse


GENDER_CHOICES = [
    ['male', u"Мужской"],
    ['female', u"Женский"],
]

REL_CHOICES = [
    ['none', u"Не определенно"],
    ['single', u"Холост"],
    ['in_a_rel', u"В отношениях"],
    ['engaged', u"Помолвлен(а)"],
    ['married', u"Женат/Замужем"],
    ['in_love', u"Влюблен(а)"],
    ['complicated', u"Все сложно"],
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  default=None, null=False, verbose_name=u"Пользователь", related_name='my_user', primary_key=True,)
    avatar = models.ImageField(verbose_name=u"Аватар", null=True, blank=True, upload_to='avatar/%Y/%m/%d/')
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name=u"О себе")
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"Город")
    birth_date = models.DateField(null=True, blank=True, verbose_name=u"Дата рождения")
    gender = models.CharField(max_length=10, verbose_name=u"Пол", choices=GENDER_CHOICES, default="male")
    relationship = models.CharField(max_length=20, verbose_name=u"Статус отношений", choices=REL_CHOICES, default="none")

    def __str__(self):
        return str(self.user) or ''


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['birth_date']

    def get_absolute_url(self): # Тут мы создали новый метод
        return reverse('profile_detail', args=[str(self.id)])