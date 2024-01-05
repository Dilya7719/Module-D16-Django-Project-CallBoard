from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DetailView
from django.urls import reverse_lazy
from .models import UserData
from .forms import ProfileForm


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    raise_exception = True
    model = UserData
    form_class = ProfileForm
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('call_list')

    def get_object(self, queryset=None):
        return UserData.objects.get(user_id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



