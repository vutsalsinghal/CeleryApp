from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import redirect

from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts
import logging
logger = logging.getLogger('general')

class UsersListView(ListView):
	template_name = 'users_list.html'
	model         = User


class GenerateRandomUserView(FormView):
	template_name = 'generate_random_users.html'
	form_class    = GenerateRandomUserForm

	def form_valid(self, form):
		total = form.cleaned_data.get('total')
		create_random_user_accounts.delay(total)
		
		logger.info('Sent request to create %d users!' %(total))
		
		messages.success(self.request, 'We are generating %s random users! Wait a moment and refresh this page.'%(total))
		return redirect('users_list')