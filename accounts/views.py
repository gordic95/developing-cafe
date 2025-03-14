from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy


from .forms import LoginForm, RegisterForm
from . models import Profile
from django.views.generic import ListView, DetailView


def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse_lazy('order:order_list'))
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def LogoutView(request):
    logout(request)
    return render(request, 'accounts/logout.html')


def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'accounts/register_done.html', {'user': user})
    else:
        form = RegisterForm(request.POST)
        return render(request, 'accounts/register.html', {'form': form})


class ProfileView(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'
    context_object_name = 'profile'


def profile_order_view(request, pk):
    queryset = Profile.objects.get(pk=pk).orders.all()
    return render(request, 'accounts/profile_orders.html', {'orders': queryset})














