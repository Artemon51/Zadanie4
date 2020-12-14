"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from.models import Comment
from.models import Blog
from.models import Zakaz


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'width: 100%;',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'width: 100%;',
                                   'placeholder':'Пароль'}))

class PoolForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=20)
    email = forms.EmailField(label='E-mail', min_length=7)
    direction = forms.ChoiceField(label='Кем вы являетесь', 
                                  choices=[
                                      ('1', 'Физическое лицо'), 
                                      ('2', 'Организация')
                                      ], widget=forms.RadioSelect, initial=1)
    topic = forms.ChoiceField(label='Тема вашего обращения', choices=(('1', 'Проблемы с аккаунтом'),
                                                        ('2', 'Удалить аккаунт'),
                                                        ('3', 'Сотрудничество'),
                                                        ('4', 'Реклама'),
                                                        ('5', 'Другое')), initial=1)
    check = forms.BooleanField(label='У вас есть аккаунт', required=False)
    info = forms.CharField(label='Текст обращения', widget=forms.Textarea(attrs={'rows':4, 'cols':30}))

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text


class BlogForm (forms.ModelForm):
    class Meta:
        model = Blog                                                            # используемая модель
        fields = ('title', 'description', 'content', 'image',)                   # заполнение поля
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание" , 'image': "Картинка"}        # метка к полю формы text


class  ZakazForm(forms.ModelForm):
    class Meta:
        model = Zakaz                                                            # используемая модель
        fields = ('name', 'number', 'pay', 'rabota', 'description','image', )                   # заполнение поля
        labels = {'name': "Ваше ФИО", 'number': "Ваш номер телефона", 'pay': "Способ оплаты" , 'rabota': "Вид работы" , 'description': "Подробнее о заказе", 'image': "Фото места работы" }        # метка к полю формы text
