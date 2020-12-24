from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from django.views import generic
from .models import  AwWinePalateFlavors,AwUserPalateWine,AwWinePalateCategories
from django.http import JsonResponse
from .serializers import  AwWinePalateFlavorsSerializear
from django.urls import reverse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from home.models import AwCmsPaage
from django.template.defaulttags import register
# Create your views here.


def payment(request):
    return render(request, 'web/payment/payment.html')

@register.filter(name='categoryes_selected_categoryes_and_flavers')
def categoryes_selected_categoryes_and_flavers(cayegory_ins_ins,user):
    get_all_falcers = None
    if AwWinePalateFlavors.objects.filter(Category__Category_name=cayegory_ins_ins.Category_name).exists():
        get_all_falcers = AwWinePalateFlavors.objects.filter(Category__Category_name=cayegory_ins_ins.Category_name)
    get_selected_flavers = []
    if AwUserPalateWine.objects.filter(User=user,Category_name=cayegory_ins_ins.Category_name).exists():
        get_data = AwUserPalateWine.objects.filter(User=user,Category_name=cayegory_ins_ins.Category_name).values('Type')
        if get_data:
            for item in get_data:
                get_selected_flavers.append(item['Type'])
    print("==================")
    print(get_selected_flavers)
    print("==================")
    content = {"Category_name":cayegory_ins_ins.Category_name,"cate_id":cayegory_ins_ins.id,"get_all_falcers":get_all_falcers,"user":user.username,"get_selected_flavers":get_selected_flavers}
    return render_to_string('web/wine_palate/selected_flavers.html',content)


@register.filter(name='get_selected_cate_ids')
def get_selected_cate_ids(user):
    get_data = ""
    selected_category_only = []
    if user.is_authenticated:
        if AwUserPalateWine.objects.filter(User=user).exists():
            get_selected_data = AwUserPalateWine.objects.filter(User=user).values('Category_name')
            for item in get_selected_data:
                if item['Category_name'] in selected_category_only:
                    pass
                else:
                    selected_category_only.append(item['Category_name'])
    if AwWinePalateFlavors.objects.filter(Category__Category_name__in=selected_category_only).exists():
        get_all_unselected_value = AwWinePalateFlavors.objects.filter(Category__Category_name__in=selected_category_only).values("id")
        for item in get_all_unselected_value:
            get_data_splite = get_data.split(",")
            if item['id'] in get_data_splite:
                pass
            else:
                get_data += str(item['id'])+","
    return get_data

class ManageWinePalateView(generic.TemplateView):
    template_name = "web/wine_palate/wine_palate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_page_info = None
        page_slug = 'palate-profile'
        if AwCmsPaage.objects.filter(Slug=page_slug).exists():
            get_page_info = get_object_or_404(AwCmsPaage, Slug=page_slug)
        context['get_page_info'] = get_page_info
        get_selected_data = None
        selected_category_only = []
        get_all_unselected_value = None
        if self.request.user.is_authenticated:
            if AwUserPalateWine.objects.filter(User=self.request.user).exists():
                get_selected_data = AwUserPalateWine.objects.filter(User=self.request.user).values('Category_name')
                for item in get_selected_data:
                    if item['Category_name'] in selected_category_only:
                        pass
                    else:
                        selected_category_only.append(item['Category_name'])
        if AwWinePalateCategories.objects.filter(Category_name__in=selected_category_only).exists():
            get_all_unselected_value = AwWinePalateCategories.objects.filter(Category_name__in=selected_category_only)
        context['selected_category_only'] = selected_category_only
        context['get_all_unselected_value'] = get_all_unselected_value
        # print(selected_category_only)
        print(get_all_unselected_value)
        return context

    def post(self, request, *args, **kwargs):
        temp_vari = ""
        get_data = request.POST.getlist("palat_profile_data[]")
        get_cate_data = request.POST.getlist("palat_profile_cate_data[]")
        if get_cate_data:
            AwUserPalateWine.objects.filter(User=request.user).filter(Category_name__in = get_cate_data).delete()
        for item in get_data:
            get_in_list = item.split('__')
            if AwUserPalateWine.objects.filter(User=request.user).filter(CategoryNameAndType=item).exists():
                text = ""
            else:
                # if temp_vari != get_in_list[1]:
                #     AwUserPalateWine.objects.filter(User = request.user).filter(Category_name=get_in_list[1]).delete()
                #     temp_vari = get_in_list[1]
                add_data = AwUserPalateWine(User = request.user,CategoryNameAndType=item,Category_name=get_in_list[1],Type=get_in_list[0])
                add_data.save()
        messages.info(request, "Palate Profile saved successfully.")
        return HttpResponseRedirect(reverse('wine_palate:wine_palate'))

@csrf_exempt
def GetWinePalatedataView(request):
    get_data = {}
    get_name = "test"
    get_user_palate_category = []
    get_user_palate_type = []
    if request.method == 'POST':
        get_name_id  = request.POST['Category_id']

        get_user_palate_category = []
        get_user_palate_type = []
        if AwUserPalateWine.objects.filter(User=request.user).exists():
            get_data_of_user = AwUserPalateWine.objects.filter(User=request.user)
            for items in get_data_of_user:
                get_user_palate_category.append(items.Category_name)
                get_user_palate_type.append(items.Type)
        if AwWinePalateFlavors.objects.filter(Category__Category_Id=get_name_id).exists():
            get_data_Ins = AwWinePalateFlavors.objects.filter(Category__Category_Id=get_name_id)
            data_scri = AwWinePalateFlavorsSerializear(get_data_Ins , many=True)
            get_data = data_scri.data
    get_name = ""
    if AwWinePalateCategories.objects.filter(Category_Id=get_name_id).exists():
        get_cate_data = get_object_or_404(AwWinePalateCategories,Category_Id=get_name_id)
        get_name = get_cate_data.Category_name
    # return render(request,"web/wine_palate/wine_palate_data.html",)
    return JsonResponse({"get_data":get_data,"get_name":get_name,"get_user_palate_category":get_user_palate_category,'get_user_palate_type':get_user_palate_type})





@csrf_exempt
def GetWinePalatedataViewByName(request):
    get_data = {}
    get_name = "test"
    get_user_palate_category = []
    get_user_palate_type = []
    if request.method == 'POST':
        get_name  = request.POST['Category']
        get_user_palate_category = []
        get_user_palate_type = []
        if AwUserPalateWine.objects.filter(User=request.user).exists():
            get_data_of_user = AwUserPalateWine.objects.filter(User=request.user)
            for items in get_data_of_user:
                get_user_palate_category.append(items.Category_name)
                get_user_palate_type.append(items.Type)
        if AwWinePalateFlavors.objects.filter(Category__Category_name=get_name).exists():
            get_data_Ins = AwWinePalateFlavors.objects.filter(Category__Category_name=get_name)
            data_scri = AwWinePalateFlavorsSerializear(get_data_Ins , many=True)
            get_data = data_scri.data
    # return render(request,"web/wine_palate/wine_palate_data.html",)
    return JsonResponse({"get_data":get_data,"get_name":get_name,"get_user_palate_category":get_user_palate_category,'get_user_palate_type':get_user_palate_type})