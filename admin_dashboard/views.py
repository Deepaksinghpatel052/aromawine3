from django.shortcuts import render,HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required , name="dispatch")
class AdminDashboardVIew(generic.TemplateView):
    template_name = 'admin/dashboard/index.html'