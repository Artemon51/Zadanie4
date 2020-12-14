"""
Definition of urls for Zadanie4.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings



urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('links/', views.links, name='links'),
    path('newpost/', views.newpost, name='newpost'),
    path('videopost/', views.videopost, name='videopost'),
    path('pool/', views.pool, name='pool'),
    path('blog/', views.blog, name='blog'),
    path('zakaz/', views.zakaz, name='zakaz'),
    path('kabinet/', views.kabinet, name='kabinet'),
    path('(?P<parametr>\d+)/$', views.blogpost, name='blogpost'),
    path('zakazpost/(?P<id>\d+)/$',views.zakazpost, name='zakazpost'),
    path('deletezakaz/(?P<delid>\d+)/$',views.deletezakaz, name='deletezakaz'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Авторизация',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('registration/', views.registration, name='registration'),

 
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()