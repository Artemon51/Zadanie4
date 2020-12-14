"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.db import models
from .models import Blog
from .models import Zakaz
from .models import Comment # использование модели комментариев
from .forms import CommentForm # использование формы ввода комментария
from .forms import BlogForm 
from .forms import ZakazForm


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Обращаться:',
            'year':datetime.now().year,
        }
    )

def links(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {   
            'message':'Наши социальные сети:',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'message':'Добро пожаловать, наша компания называется «Океан»!',
            'year':datetime.now().year,
        }
    )
from .forms import PoolForm 

def pool(request):
    assert isinstance(request, HttpRequest)
    data = None
    direction = {'1': 'Физическое лицо', '2': 'Организация'}
    topic = {'1': 'Проблемы с аккаунтом', '2': 'Удалить аккаунт', '3': 'Сотрудничество', '4': 'Реклама', '5': 'Другое'}

    if request.method == 'POST':
        form = PoolForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['email'] = form.cleaned_data['email']
            data['direction'] = direction[ form.cleaned_data['direction'] ]
            data['topic'] = topic[ form.cleaned_data['topic'] ]

            if (form.cleaned_data['check'] == True):
                data['check'] = 'Имеется'
            else:
                data['check'] = 'Отсутствует'
            data['info'] = form.cleaned_data['info']
            form = None
    else:
        form = PoolForm()

    return render(
        request,
        'app/pool.html',
        {
            'form':form,
            'data':data,
            'year': datetime.now().year, 
        }
    )

def registration(request):
    """Renders the registration page."""

    assert isinstance(request, HttpRequest)
    if request.method == "POST": # после отправки формы
        regform = UserCreationForm (request.POST)
        if regform.is_valid(): #валидация полей формы
            reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы
            reg_f.is_staff = False # запрещен вход в административный раздел
            reg_f.is_active = True # активный пользователь
            reg_f.is_superuser = False # не является суперпользователем
            reg_f.date_joined = datetime.now() # дата регистрации
            reg_f.last_login = datetime.now() # дата последней авторизации
            reg_f.save() # сохраняем изменения после добавления данных
            return redirect('home') # переадресация на главную страницу после регистрации
    else:
        regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя
    return render(
        request,
        'app/registration.html',
        {
            'regform': regform, # передача формы в шаблон веб-страницы
            'year':datetime.now().year,
        }
)

def blog(request):
    """Renders the about page."""
    posts = Blog.objects.all()            #запрос на выбор всех статей из модели

    assert isinstance (request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        {
            'title':'Блог',
            'posts': posts,                  #передача списка статей в шаблон веб-страницы
            'year': datetime.now().year, 
            }
    )                              


def blogpost(request, parametr):
    """Renders the about page."""
    post_1 = Blog.objects.get(id=parametr)            #запрос на выбор конкретной статьи по параметру
    comments = Comment.objects.filter(post=parametr) #запрос на выбор всех комментариев статьи
  
    if request.method == "POST": # после отправки данных формы на сервер методом POST
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя
            comment_f.date = datetime.now() # добавляем в модель Комментария (Comment) текущую дату
            comment_f.post = Blog.objects.get(id=parametr) # добавляем в модель Комментария (Comment) статью, для которой данный комментарий
            comment_f.save() # сохраняем изменения после добавления полей
            return redirect('blogpost', parametr=post_1.id) # переадресация на ту же страницу статьи после отправки комментария
    else:
        form = CommentForm() # создание формы для ввода комментария
    
    
    assert isinstance (request, HttpRequest)
    return render(
        request,
        'app/blogpost.html',
        {
            'post_1':post_1,                 #передача конкретной статьи в шаблон веб-страницы 
            'comments': comments,            # передача всех комментариев к данной статье в шаблон веб-страницы
            'form': form,                    # передача формы добавления комментария в шаблон веб-страницы
            'year': datetime.now().year, 
        }
    )    

def newpost(request):
    assert isinstance(request, HttpRequest)

    if request.method == "POST":                # после отправки формы
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.author = request.user
            blog_f.save()                        # сохраняем изменения после добавления полей

            return redirect('blog')              # переадресация на страницу Блог после создания статьи
    else:
        blogform = BlogForm()                     # создание объекта формы для ввода данных

    return render(
        request,
        'app/newpost.html',
        {
            'blogform': blogform,           # передача формы в шаблон веб-страницы
            'title': 'Добавить статью болга',
            'year': datetime.now().year,
        }
    )

def videopost(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
         
            'year':datetime.now().year,
        }
    )


def zakaz(request):
    assert isinstance(request, HttpRequest)

    if request.method == "POST":                # после отправки формы
        zakazform = ZakazForm(request.POST, request.FILES)
        if zakazform.is_valid():
            zakaz_f = zakazform.save(commit=False)
            zakaz_f.posted = datetime.now()
            zakaz_f.author = request.user
            zakaz_f.status = False
            zakaz_f.save()                        # сохраняем изменения после добавления полей

            return redirect('home')              # переадресация на страницу Блог после создания статьи
    else:
        zakazform = ZakazForm()                     # создание объекта формы для ввода данных

    return render(
        request,
        'app/zakaz.html',
        {
            'zakazform': zakazform,           # передача формы в шаблон веб-страницы
            'year': datetime.now().year,
        }
    )

def kabinet(request):
    posts = Zakaz.objects.filter(author = request.user)            #запрос на выбор всех статей из модели

    assert isinstance (request, HttpRequest)
    return render(
        request,
        'app/kabinet.html',
        {
            'posts': posts,                  #передача списка статей в шаблон веб-страницы
            'year': datetime.now().year, 
            }
    )

def zakazpost(request, id):
    posts = Zakaz.objects.filter(id = id)            #запрос на выбор всех статей из модели

    assert isinstance (request, HttpRequest)
    return render(
        request,
        'app/zakazpost.html',
        {
            'posts': posts,                  #передача списка статей в шаблон веб-страницы
            'year': datetime.now().year, 
            }
    )

def deletezakaz(request,delid):
    assert isinstance (request, HttpRequest)

    query = Zakaz.objects.get(id=delid)
    query.delete()
    return redirect('kabinet') 