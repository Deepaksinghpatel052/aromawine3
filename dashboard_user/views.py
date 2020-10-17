from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from profile_user.models import AwUserInfo
from orders.models import AwOrders,AwOrederItem
from admin_mambership_setting.models import AwMembership
from django.db.models import Sum
# Create your views here.
@method_decorator(login_required , name="dispatch")
class DashboardView(generic.TemplateView):
	template_name = "web/user/page/dashboard/dashboard.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		user_info = None
		letest_order= None
		celler_item = None
		if AwUserInfo.objects.filter(User=self.request.user).exists():
			user_info = get_object_or_404(AwUserInfo, User=self.request.user)

		if AwOrders.objects.filter(User=self.request.user).exists():
			letest_order = AwOrders.objects.filter(User=self.request.user).order_by("-id").first()

		if AwOrederItem.objects.filter(User=self.request.user).filter(Order_id__Order_Type='Caller').exists():
			celler_item = AwOrederItem.objects.filter(User=self.request.user).filter(Order_id__Order_Type='Caller').order_by("-id")[:5]
		context['letest_order'] = letest_order
		context['user_info'] = user_info
		context['celler_item'] = celler_item
		context['Page_title'] = self.request.user.username+"-dashboard"

		total_amount = 0

		membership_label  = None

		if AwOrders.objects.filter(User=self.request.user).filter(Payment_Status=True).exists():
			total_order_amount = AwOrders.objects.filter(User=self.request.user).filter(Payment_Status=True).aggregate(Sum('Amount'))
			total_amount = total_order_amount['Amount__sum']

		if AwMembership.objects.filter(min_price__lte=total_amount,max_price__gte=total_amount).exists():
			membership_label = get_object_or_404(AwMembership,min_price__lte=total_amount,max_price__gte=total_amount)
		context['membership_label'] = membership_label
		return context