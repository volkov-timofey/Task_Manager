from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = messages.get_messages(self.request)
        return context


class LoginUserView(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_message = _('Вы залогинены')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = messages.get_messages(self.request)
        return context

    def get_success_url(self):
        return reverse_lazy('index')


class LogoutUserView(LogoutView):
    success_message = _('Вы разлогинены')

    def get_success_url(self):
        return reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.SUCCESS, self.success_message)
        return response
