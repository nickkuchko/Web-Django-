from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout

from .forms import ContactForm, LoginForm, NewUserForm
from .models import *

menu = [{'title': "News", 'url_name': 'news'},
        {'title': "About this web", 'url_name': 'about'},
        {'title': "Store", 'url_name': 'store'},
        {'title': "Contact me", 'url_name': 'contact'},
        ]


def index(request):
    posts = Book.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': "Main"
    }
    return render(request, 'app1/index.html', context=context)


def news(request):
    nws = News.objects.all()
    context1 = {
        'news': nws,
        'menu': menu,
        'title': "News"
    }
    return render(request, 'app1/news.html', context=context1)


def about(request):
    return render(request, 'app1/about.html', {'menu': menu, 'title': "About"})

def store(request):
    return render(request, 'app1/store.html', {'menu': menu, 'title': "Store"})

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email,
                          ['admin@example.com'])                 # this is an example. Should use real email here
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "app1/contact.html", {'form': form})

def success(request):
    return render(request, 'app1/success.html')


def show_post(request, post_slug):
    post = get_object_or_404(Book, slug=post_slug)  # function get objects from Book with key slug, else 404
    context = {
        'post': post,
        'menu': menu,
    }
    return render(request, 'app1/post.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> There is no such page </h1>")


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect('home')
                else:
                    return HttpResponse('Disabled account')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'app1/login.html', {'form': form})


def logout_request(request):
    logout(request)
    return redirect("home")


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="app1/register.html", context={"register_form":form})
