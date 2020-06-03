from django.shortcuts import render, redirect
from .forms import LoginForm, UserRegistrationForm
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from articles.models import Article, Comment

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return render(request, 'articles/index', {'form': form})
                    # return redirect('articles/index')
                    return HttpResponseRedirect(reverse('articles:index'))
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'log_in/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'log_in/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'log_in/register.html', {'user_form': user_form})