from django.shortcuts import render,HttpResponseRedirect
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import AwAdminSetting,AwManageShipping
from .forms import AwAdminSettingForm,AwManageShippingForm
from .serializers import ApiWineProjectInfoSerializers
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.template.defaulttags import register
from django.template.loader import render_to_string
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.



# API Start================
class ApiWineProjectInfo(APIView):

    def get(self,request):
        project_info = {}
        if AwAdminSetting.objects.all().exists():
            get_data = AwAdminSetting.objects.all().first()
            get_res_sri = ApiWineProjectInfoSerializers(get_data,context={"request": request})
            project_info = get_res_sri.data
        return Response({"data":project_info},status=200)
# API END================


@register.filter(name='get_logo')
def get_logo(demo):
    logo_image = settings.BASE_URL+"static/web/assets/image/wine-logo.svg"
    if AwAdminSetting.objects.all().exists():
        get_data = AwAdminSetting.objects.all().first()
        if get_data.Logo:
            logo_image = get_data.Logo.url
    return str(logo_image)

@register.filter(name='get_favicon')
def get_favicon(demo):
    logo_image = settings.BASE_URL+"static/web/assets/image/logo.png"
    if AwAdminSetting.objects.all().exists():
        get_data = AwAdminSetting.objects.all().first()
        if get_data.favicon:
            logo_image = get_data.favicon.url
    return str(logo_image)





@register.filter(name='get_project_name')
def get_project_name(demo):
    project_name = "AROMA OF WINE"
    if AwAdminSetting.objects.all().exists():
        get_data = AwAdminSetting.objects.all().first()
        if get_data.Project_Name:
            project_name = get_data.Project_Name
    return str(project_name)

@register.filter(name='get_tag_line')
def get_tag_line(demo):
    project_tag_line = "Wine inspired by your palate"
    if AwAdminSetting.objects.all().exists():
        get_data = AwAdminSetting.objects.all().first()
        if get_data.Project_Tag_Line:
            project_tag_line = get_data.Project_Tag_Line
    return str(project_tag_line)




@register.filter(name='get_GST')
def get_GST(demo):
    get_GST_amount = "0"
    if AwAdminSetting.objects.all().exists():
        get_data = AwAdminSetting.objects.all().first()
        if get_data.GST:
            get_GST_amount = get_data.GST
    return str(get_GST_amount)


@register.filter(name='get_duty')
def get_duty(demo):
    get_duty_amount = "0"
    if AwAdminSetting.objects.all().exists():
        get_data = AwAdminSetting.objects.all().first()
        if get_data.Duty:
            get_duty_amount = get_data.Duty
    return str(get_duty_amount)




@register.filter(name='get_analytics')
def get_analytics(demo):
    get_analytics_data = ""
    if AwAdminSetting.objects.all().exists():
        get_data = AwAdminSetting.objects.all().first()
        if get_data.Analytics:
            get_analytics_data = get_data.Analytics
    return str(get_analytics_data)



@register.filter(name='get_social_media_info')
def get_social_media_info(demo):
    get_data = ""
    if AwAdminSetting.objects.all().exists():
        get_data = AwAdminSetting.objects.all().first()
    return render_to_string('web/home/social_media_link.html', {"get_data":get_data})



@method_decorator(login_required , name="dispatch")
class ManageGeneralSettingView(SuccessMessageMixin,generic.CreateView):
    form_class = AwAdminSettingForm
    template_name = 'admin/setting/general.html'


    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "General add successfully."
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "General Setting"
        return context

    def dispatch(self, request, *args, **kwargs):
        if AwAdminSetting.objects.all().exists():
            get_data = AwAdminSetting.objects.all().first()
            return HttpResponseRedirect(reverse('admin_manage_setting:update_general',args=(get_data.id,)))
        else:
            return super(ManageGeneralSettingView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        messages.info(self.request, 'Update successfully.')
        # success_url = reverse_lazy('admin_manage_setting:update_general' self.kwargs['pk'])
        return HttpResponseRedirect(reverse('admin_manage_setting:update_general',args=(self.object.id,)))


@method_decorator(login_required, name="dispatch")
class GeneralUpdateView(SuccessMessageMixin, generic.UpdateView):
    form_class = AwAdminSettingForm
    template_name = 'admin/setting/general.html'
    queryset = AwAdminSetting.objects.all()

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "update successfully."

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['Page_title'] = "General Setting"
        return context

    def form_valid(self, form):
        self.object = form.save()
        messages.info(self.request, 'Update successfully.')
        # success_url = reverse_lazy('admin_manage_setting:update_general' self.kwargs['pk'])
        return HttpResponseRedirect(reverse('admin_manage_setting:update_general',args=(self.kwargs['pk'],)))




@method_decorator(login_required , name="dispatch")
class ManageShippingSettingView(SuccessMessageMixin,generic.TemplateView):
    # queryset = AwProducers.objects.all().order_by("-id")
    form_class = AwManageShippingForm
    template_name = 'admin/setting/shipping.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        queryset = AwManageShipping.objects.all().order_by("-id")
        return render(request, self.template_name,{'form_class': form, 'Page_title': "Manage Shipping", "object": queryset})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        queryset = AwManageShipping.objects.all().order_by("-id")
        if form.is_valid():
            Shipping_ins = form.save(commit=False)
            Shipping_ins.Created_by = request.user
            Shipping_ins.save()
            form.save_m2m()
            messages.info(request, "Shipping add successfully.")
        return render(request, self.template_name,
                          {'form_class': form, "object": queryset, 'Page_title': "Manage Shipping"})



class ShippingDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = AwManageShipping
    template_name = 'admin/setting/shipping_delete.html'
    success_url = reverse_lazy('admin_manage_setting:shipping')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Delete shipping"
        return context
    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "shipping remove successfully."



def update_shipping(request):
    if request.method == 'POST':
        ids = request.POST.getlist('ids[]')
        Free_Shipping_Amount = request.POST.getlist('Free_Shipping_Amount[]')
        Free_Flat_Shipping = request.POST.getlist('Free_Flat_Shipping[]')
        for i in range(0,len(ids)):
            AwManageShipping.objects.filter(id=ids[i]).update(Free_Shipping_Amount=Free_Shipping_Amount[i],Free_Flat_Shipping=Free_Flat_Shipping[i])
        messages.info(request, "Shipping update successfully.")
    return redirect(settings.BASE_URL+"admin/settings/fee-shipping")
