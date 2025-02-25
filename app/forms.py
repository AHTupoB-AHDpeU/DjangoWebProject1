"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment, Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class AnketaForm(forms.Form):
    name = forms.CharField(label='Baшe ФИО', min_length=2, max_length=100)
    city = forms.CharField(label='Baш гopoд', min_length=2, max_length=100)
    theme = forms.ChoiceField(label='Выберите тему обращения',
                               choices=[('1', 'Покупка товара'), ('2', 'Доставка товара'), ('3', 'Сервисный центр'), ('4', 'Ошибки сайта'), ('5', 'Оценка работы')], 
                               widget=forms. RadioSelect, initial=1)
    internet = forms.ChoiceField(label='Откуда вы узнали о нашем Интернет-магазине?',
                                 choices=(('1', 'По совету знакомых/друзей'),
                                 ('2', 'Реклама в Интернете'),
                                 ('3', 'Социальные сети'),
                                 ('4', 'Случайно')), initial=1)
    notice = forms.BooleanField(label='Прислать ответ на E-Mail',
                                required=False)
    notice1 = forms.BooleanField(label='Прислать ответ в виде SMS',
                                required=False)
    email = forms.EmailField (label='Baш e-mail для связи', min_length=7)
    phone = forms.CharField(label='Ваш номер телефона', min_length=11)
    message = forms.CharField(label='Текст сообщения',
                              widget=forms.Textarea (attrs={'rows' :12, 'cols':20}))

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}