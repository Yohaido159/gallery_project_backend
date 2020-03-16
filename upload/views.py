from users.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect

from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts


class GenerateRandomUserView(FormView):
    template_name = 'upload/generate_random_users.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(
            self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('/')
