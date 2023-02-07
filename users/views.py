from datetime import datetime

import pytz
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from users.forms import SigninForm, SignupForm
from users.models import User
from users.service import set_verify_token_and_send_mail


class SigninView(LoginView):
    template_name = 'users/login.html'
    form_class = SigninForm


class SignupView(CreateView):
    template_name = 'users/register.html'
    model = User
    form_class = SignupForm
    success_url = reverse_lazy('users:register_success')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            set_verify_token_and_send_mail(self.object)
        return super().form_valid(form)


class SignupSuccessView(TemplateView):
    template_name = 'users/signup_success.html'


class VerifySuccessView(TemplateView):
    template_name = 'users/verify_success.html'


def verify_email(request, token):
    current_user = User.objects.filter(verify_token=token).first()
    if current_user:
        now = datetime.now(pytz.timezone(settings.TIME_ZONE))
        if now > current_user.verify_token_expired:
            # TODO: сделать воркер на зачистку тех, кто пробаранил 3 дня
            current_user.delete()
            return render(request, 'users/verify_token_expired.html')

        current_user.is_active = True
        current_user.verify_token = None
        current_user.verify_token_expired = None
        current_user.save()
        # TODO: редирект на логин
        # login(request, current_user)
        # return render(request, 'users/verify_token_success.html')
        # TODO: потом авторизовать и кинуть на главную
        return redirect('users:login')

    return render(request, 'users/verify_failed.html')
