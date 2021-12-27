from django.urls import path

from .views import *
from . import views

urlpatterns = [
    path('', index, name='home'),
    path('news/', news, name='news'),
    path('about/', about, name='about'),
    path('store/', store, name='store'),
    path('contact/', contact, name='contact'),
    path('success/', success, name='success'),  # when the email from the contact form is sent successfully
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_request, name="logout"),  # there is redirection to home page in views.py. logout.html is created just for any cases, it doesn't used now
    path("register/", views.register_request, name="register"),
    path('post/<slug:post_slug>/', show_post, name='post'),  # home page posts opened in new page
]

