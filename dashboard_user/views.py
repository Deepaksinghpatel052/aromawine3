from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(login_required , name="dispatch")
class DashboardView(generic.TemplateView):
	template_name = "web/user/page/dashboard/dashboard.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['Page_title'] = self.request.user.username+"-dashboard"
		return context