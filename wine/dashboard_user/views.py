from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(login_required , name="dispatch")
class DashboardView(generic.TemplateView):
	template_name = "web/user/page/dashboard/dashboard.html"