from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



#  ----------- Handling the login/logout  request ---------------------

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('home')

class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'
    success_url = reverse_lazy('logout')


#  ----------- Handling the password reset request ---------------------

class PResetView(PasswordResetView):
    template_name = 'users/password_reset.html'

class PResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'

class PResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'

class PResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'
