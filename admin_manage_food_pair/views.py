from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from .models import AwFoodpair
from .forms import AwFoodpairForm
from django.urls import reverse
from django.urls import reverse_lazy


@method_decorator(login_required , name="dispatch")
class ManageFoodPairView(SuccessMessageMixin,generic.View):
    form_class = AwFoodpairForm
    template_name = "admin/foodpair/index_food_pair.html"


    def get(self, request, *args, **kwargs):
        form = self.form_class
        queryset = AwFoodpair.objects.all().order_by("-id")
        return render(request, self.template_name, {'form_class': form,'Page_title':"Manage Food Pair","object":queryset})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        queryset = AwFoodpair.objects.all().order_by("-id")
        if form.is_valid():
            form.save()
            messages.info(request, "Food Pair add successfully.")
            return HttpResponseRedirect(reverse('admin_manage_food_pair:foodpair'))
        else:
            return render(request, self.template_name, {'form_class': form,"object":queryset,'Page_title':"Manage Food Pair"})






@method_decorator(login_required , name="dispatch")
class foodpairUpdateView(SuccessMessageMixin,generic.UpdateView):
    form_class = AwFoodpairForm
    template_name = 'admin/foodpair/edit_foodpair.html'
    queryset = AwFoodpair.objects.all()
    success_url = reverse_lazy('admin_manage_food_pair:foodpair')

    def get_success_message(self, cleaned_data):
        return "Food Pair update successfully."
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Edit Food Pair"
        return context
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Updated_by = self.request.user
        return super().form_valid(form)
    def form_invalid(self, form):
        response = super(foodpairUpdateView, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            messages.error(self.request, form.errors)
            return HttpResponseRedirect(reverse('admin_manage_food_pair:foodpair'))



class FoodpairDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = AwFoodpair
    template_name = 'admin/foodpair/delete_foodpair.html'
    success_url = reverse_lazy('admin_manage_food_pair:foodpair')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Delete Food Pair"
        return context
    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Food Pair remove successfully."
