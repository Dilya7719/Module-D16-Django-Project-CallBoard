from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from .models import Call, Respond
from .filters import CallFilter, CallFilterForResponds
from .forms import CallForm, RespondForm


class CallsList(ListView):
    """Все объявления"""
    model = Call
    ordering = '-call_create_date'
    template_name = 'calls.html'
    context_object_name = 'calls'
    paginate_by = 8

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CallFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class CallCreate(LoginRequiredMixin, CreateView):
    """Создание объявления"""
    raise_exception = True
    form_class = CallForm
    model = Call
    template_name = 'call_create.html'

    def form_valid(self, form):
        form.instance.call_author = self.request.user
        return super().form_valid(form)


class CallUpdate(LoginRequiredMixin, UpdateView):
    """Редактирование объявления"""
    raise_exception = True
    form_class = CallForm
    model = Call
    template_name = 'call_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Признак объявления пользователя для защиты от редактирования другими пользователями
        context['is_my_call'] = Call.objects.get(id=self.kwargs['pk']).call_author == self.request.user
        return context


class CallDelete(LoginRequiredMixin, DeleteView):
    """Удаление объявления"""
    raise_exception = True
    model = Call
    template_name = 'call_delete.html'
    success_url = reverse_lazy('call_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Признак объявления пользователя для защиты от удаления другими пользователями
        context['is_my_call'] = Call.objects.get(id=self.kwargs['pk']).call_author == self.request.user
        return context


class MyCallsList(ListView):
    """Список объявлений пользователя"""
    model = Call
    template_name = 'my_calls.html'
    context_object_name = 'calls'
    paginate_by = 8

    def get_queryset(self):
        queryset = Call.objects.filter(call_author=self.request.user.id).order_by('-call_create_date')
        self.filterset = CallFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class RespondSend(LoginRequiredMixin, CreateView):
    """Просмотр объявления + создание отклика"""
    raise_exception = True
    form_class = RespondForm
    model = Respond
    template_name = 'respond.html'

    def form_valid(self, form):
        form.instance.respond_author = self.request.user
        form.instance.respond_call = Call.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return '/calls/'+ str(self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['call'] = Call.objects.get(id=self.kwargs['pk'])
        # Получаем все принятые отклики на текущее объявление, за исключением авторских
        context['responds'] = Respond.objects.filter(respond_call=Call.objects.get(id=self.kwargs['pk'])).exclude(
            respond_author=self.request.user).filter(respond_accept=True)
        # Получаем все авторские отклики без исключений
        context['my_responds'] = Respond.objects.filter(respond_call=Call.objects.get(id=self.kwargs['pk'])).filter(
            respond_author=self.request.user)
        # Получаем все отклики кроме авторских, кроме непринятых
        context['my_responds_edit'] = Respond.objects.filter(
            respond_call=Call.objects.get(id=self.kwargs['pk'])).exclude(respond_accept=False)
        context['is_my_call'] = Call.objects.get(id=self.kwargs['pk']).call_author == self.request.user
        return context


class MyRespondList(LoginRequiredMixin, ListView):
    """Все отклики на объявления пользователя"""
    raise_exception = True
    model = Respond
    template_name = 'my_responds.html'
    context_object_name = 'responds'

    def get_queryset(self):
        queryset = Respond.objects.filter(respond_call__call_author_id=self.request.user.id).exclude(respond_accept=False)
        self.filterset = CallFilterForResponds(self.request.GET, queryset, request=self.request.user.id)
        if self.request.GET:
            return self.filterset.qs
        return Respond.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


def respond_accept_yes(request, pk):
    """Принятие отклика"""
    respond = Respond.objects.get(id=pk)
    respond.respond_accept = True
    respond.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def respond_accept_no(request, pk):
    """Отклонение отклика"""
    respond = Respond.objects.get(id=pk)
    respond.respond_accept = False
    respond.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

