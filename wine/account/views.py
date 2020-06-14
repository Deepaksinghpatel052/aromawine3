from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from account.forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect
# Create your views here. # 
class AccountCraetLoginView(generic.TemplateView):
	form_class = SignUpForm
	template_name = "web/account/create_login.html"

	def get(self, request, *args, **kwargs):
		return render(request,self.template_name, {'form': self.form_class})

	def post(self, request, *args, **kwargs):
		if "password2" in self.request.POST:
			form = self.form_class(request.POST)
			if form.is_valid():
				form.save()
				messages.info(request,"account Created Successfuly.")
				success_url = reverse_lazy('account')
			else:
				messages.error(request, form.errors)
			return render(request, self.template_name, {'form': form})
		else:
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				if user.is_superuser:
					messages.error(request, "This login area is not used for superadmin.")
				else:
					if user.is_active:
						login(request, user)
						return HttpResponseRedirect('/user/dashboard/')
					else:
						messages.error(request, "Inactive user.")
			else:
				messages.error(request, "Please enter a correct username and password. Note that both fields may be case-sensitive.")
			return render(request, self.template_name, {'form': self.form_class})


class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")

