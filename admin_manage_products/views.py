from django.shortcuts import render,HttpResponseRedirect,HttpResponse,get_object_or_404
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import AwProducts,AwProductImage,AwProductPrice,AwProductImageFullView,AwProductReviews
from .forms import AwProductsForm
from admin_manage_Vintages.models import AwVintages
from django.contrib import messages
from django.urls import reverse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from datetime import date
import json
from admin_manage_classification.models import AwClassification
from django.template.defaulttags import register
from django.urls import reverse_lazy
from django.core.files.base import ContentFile
import base64
from django.template.loader import render_to_string
from django.db.models import Q

import requests



@csrf_exempt
def get_product_vintage(request):
    get_vintage = None
    get_selected_years = request.POST.getlist('selected_year[]')
    if AwVintages.objects.all():
        get_vintage = AwVintages.objects.all()
    return render(request,"admin/products/vintage_year.html",{"get_vintage":get_vintage,'get_selected_years':get_selected_years})


@csrf_exempt
def get_product_classifications(request):
    get_classifications = None
    classifications = request.POST.getlist('classifications[]')
    get_all_classification = []
    if AwClassification.objects.all():
        get_classifications = AwClassification.objects.all()
        for item in get_classifications:
            get_all_classification.append(item.Classification_Name)
    return render(request,"admin/products/classification.html",{"get_classifications":get_classifications,'classifications':classifications,'get_all_classification':get_all_classification})




# Create your views here.
@register.filter(name='get_product_image')
def get_product_image(product_ins):
    get_image = ""
    if product_ins:
        if AwProductImage.objects.filter(Product=product_ins).exists():
            get_product_image = AwProductImage.objects.filter(Product=product_ins).filter(Image_Type="Product_image")
            if get_product_image:
                get_image = get_product_image[0].Image.url
    data_content = {"product_image":get_image}
    return render_to_string('admin/products/product_image.html', data_content)


def get_review(lwine_code_get):
    url = "https://sandbox-api.liv-ex.com/critic/data/v1/criticData"

    # lwine_code = "10660292010"
    lwine_code = lwine_code_get
    publication_type = "Publication 1"
    payload = "{\r\n \"criticData\": {\r\n \"lwin\": \""+str(lwine_code)+"\",\r\n \"publication\": \""+str(publication_type)+"\",\r\n \"reviewer\": \"\",\r\n \"includeHistoric\": \"true\"\r\n }\r\n}\r\n"
    headers = {
        'CLIENT_KEY': '52fbdab1-9145-4fe9-8a93-27c70bd7577a',
        'CLIENT_SECRET': '5YcyXPEj',
        'ACCEPT': 'application/json',
        'CONTENT-TYPE': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    get_review = json.loads(response.text)
    if get_review['status'] == "OK":
        if 'criticData' in get_review:
            criticData = get_review['criticData']
            publication = criticData[0]['publicationData'][0]['publication']
            criticPublicationReview = criticData[0]['publicationData'][0]['publicationReview'][0]
            if AwProductReviews.objects.filter(LWineCode=lwine_code).filter(Publication=publication).filter(reviewDate=criticPublicationReview['reviewDate']).exists():
                text = "test"
            else:
                add_review = AwProductReviews(LWineCode=lwine_code,Publication=publication,reviewer=criticPublicationReview['reviewer'],reviewDate=criticPublicationReview['reviewDate'],
                                              scoreRaw=criticPublicationReview['scoreRaw'],scoreFrom=criticPublicationReview['scoreFrom'],scoreTo=criticPublicationReview['scoreTo'],
                                              scoreMedian=criticPublicationReview['scoreMedian'],drinkFrom=criticPublicationReview['drinkFrom'],drinkTo=criticPublicationReview['drinkTo'],tastingNote=criticPublicationReview['tastingNote'],
                                              externalReference=criticPublicationReview['externalReference'],externalLink=criticPublicationReview['externalLink'],externalId=criticPublicationReview['externalId'])
                add_review.save()

    # ==============================================================================================
    publication_type = "Publication 2"
    payload = "{\r\n \"criticData\": {\r\n \"lwin\": \"" + str(lwine_code) + "\",\r\n \"publication\": \"" + str(
        publication_type) + "\",\r\n \"reviewer\": \"\",\r\n \"includeHistoric\": \"true\"\r\n }\r\n}\r\n"
    headers = {
        'CLIENT_KEY': '52fbdab1-9145-4fe9-8a93-27c70bd7577a',
        'CLIENT_SECRET': '5YcyXPEj',
        'ACCEPT': 'application/json',
        'CONTENT-TYPE': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    get_review = json.loads(response.text)
    if get_review['status'] == "OK":
        if 'criticData' in get_review:
            criticData = get_review['criticData']
            publication = criticData[0]['publicationData'][0]['publication']
            criticPublicationReview = criticData[0]['publicationData'][0]['publicationReview'][0]
            if AwProductReviews.objects.filter(LWineCode=lwine_code).filter(Publication=publication).filter(
                    reviewDate=criticPublicationReview['reviewDate']).exists():
                text = "test"
            else:
                add_review = AwProductReviews(LWineCode=lwine_code, Publication=publication,
                                              reviewer=criticPublicationReview['reviewer'],
                                              reviewDate=criticPublicationReview['reviewDate'],
                                              scoreRaw=criticPublicationReview['scoreRaw'],
                                              scoreFrom=criticPublicationReview['scoreFrom'],
                                              scoreTo=criticPublicationReview['scoreTo'],
                                              scoreMedian=criticPublicationReview['scoreMedian'],
                                              drinkFrom=criticPublicationReview['drinkFrom'],
                                              drinkTo = criticPublicationReview['drinkTo'],
                                              tastingNote=criticPublicationReview['tastingNote'],
                                              externalReference=criticPublicationReview['externalReference'],
                                              externalLink=criticPublicationReview['externalLink'],
                                              externalId=criticPublicationReview['externalId'])
                add_review.save()
    return True



@method_decorator(login_required , name="dispatch")
class LowStockView(SuccessMessageMixin,generic.ListView):
    template_name = 'admin/products/low_stock.html'
    queryset = None

    def get_queryset(self,**kwargs):
        get_data = None
        get_les_then = 5
        if "les_then" in self.request.GET:
            get_les_then = self.request.GET['les_then']
        if AwProductPrice.objects.filter(Retail_Stock__lt=int(get_les_then)).exists():
            get_data = AwProductPrice.objects.filter(Retail_Stock__lt=int(get_les_then))
        return get_data


    def get_context_data(self, *args, **kwargs):
        context = super(LowStockView, self).get_context_data(*args, **kwargs)
        context['Page_title'] = "Low Stock Product"
        context['stock_range'] = ["5","10","15","20","25"]
        get_les_then = 5
        if "les_then" in self.request.GET:
            get_les_then = self.request.GET['les_then']
        context['get_les_then'] = get_les_then
        return context



@method_decorator(login_required , name="dispatch")
class OutOfStockView(SuccessMessageMixin,generic.ListView):
    template_name = 'admin/products/out_of_stock.html'
    queryset = None

    def get_queryset(self,**kwargs):
        get_data = None
        if AwProductPrice.objects.filter(Retail_Stock__lt=1).exists():
            get_data = AwProductPrice.objects.filter(Retail_Stock__lt=1)
        return get_data


    def get_context_data(self, *args, **kwargs):
        context = super(OutOfStockView, self).get_context_data(*args, **kwargs)
        context['Page_title'] = "Out Of Stock Product"
        print(context)
        return context




@method_decorator(login_required , name="dispatch")
class ManageProductsView(SuccessMessageMixin,generic.ListView):
    template_name = 'admin/products/index.html'
    queryset = AwProducts.objects.all().order_by("-id")



    def get_context_data(self, *args,**kwargs):
        context  = super(ManageProductsView,self).get_context_data(*args,**kwargs)
        context['Page_title'] = "Manage Product"
        print(context)
        return context

@method_decorator(login_required , name="dispatch")
class CreateProductView(SuccessMessageMixin,generic.View):
    template_name = 'admin/products/create.html'
    form_class = AwProductsForm
    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name,{'Page_title': "Add Product", 'form':form})

    def post(self, request, *args, **kwargs):
        form = AwProductsForm(request.POST)
        if form.is_valid():
            product_ins = form.save(commit=False)
            if request.POST["product_status"] == "Activate":
                product_ins.Status = True
            else:
                product_ins.Status = False
            product_ins.save()
            form.save_m2m()

            # ========================== add images CODE START================================
            if "product_images[]" in request.POST:
                if request.POST["product_images[]"]:
                    i=0
                    for items in request.POST.getlist('product_images[]'):
                        format, imgstr = items.split(';base64,')
                        ext = format.split('/')[-1]
                        dateTimeObj = datetime.now()
                        today_date = date.today()
                        set_file_name = str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year) + "_" + str(dateTimeObj.microsecond)
                        file_name = set_file_name + "." + ext
                        data = ContentFile(base64.b64decode(imgstr), name=file_name)
                        # if i == 0:
                        #     product_ins.Product_image.delete(save=False)
                        #     product_ins.Product_image = data
                        #     product_ins.save()
                        # else:
                        add_image = AwProductImage(Product=product_ins, Image_Type="Product_image", Image=data)
                        add_image.save()
                        i = i + 1

            if request.POST["product_banner_image"]:
                format_banner, imgstr_banner = request.POST["product_banner_image"].split(';base64,')
                ext_banner = format_banner.split('/')[-1]
                dateTimeObj_banner = datetime.now()
                today_date = date.today()
                set_file_name_banner = str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year) + "_" + str(dateTimeObj_banner.microsecond)
                file_name_banner = set_file_name_banner + "." + ext_banner
                data_banner = ContentFile(base64.b64decode(imgstr_banner), name=file_name_banner)
                add_image = AwProductImage(Product=product_ins, Image_Type="Product_Banner_image", Image=data_banner)
                add_image.save()


            if request.POST["product_thumbnail_image"]:
                format_thumbnail, imgstr_thumbnail = request.POST["product_thumbnail_image"].split(';base64,')
                ext_thumbnail = format_thumbnail.split('/')[-1]
                dateTimeObj_thumbnail = datetime.now()
                today_date = date.today()
                set_file_name_thumbnail = str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year) + "_" + str(dateTimeObj_thumbnail.microsecond)
                file_name_thumbnail = set_file_name_thumbnail + "." + ext_thumbnail
                data_thumbnail = ContentFile(base64.b64decode(imgstr_thumbnail), name=file_name_thumbnail)
                product_ins.Product_image.delete(save=False)
                product_ins.Product_image = data_thumbnail
                product_ins.save()
            # ========================== add images CODE END================================
            # ========================== add Price CODE END================================
            if request.POST.getlist('Vintage'):
                get_vintage_year = AwVintages.objects.filter(id__in=request.POST.getlist('Vintage'))
                if get_vintage_year:
                    for years in get_vintage_year:
                        if str(years.Vintages_Year) + "_bottle[]" in request.POST:
                            i = 0
                            for items in request.POST.getlist(str(years.Vintages_Year) + "_bottle[]"):
                                add_price = AwProductPrice(
                                    Product = product_ins,
                                    Vintage_Year = years,
                                    Bottle = str(request.POST.getlist(str(years.Vintages_Year) + "_bottle[]")[i]),
                                    Retail_Cost = str(request.POST.getlist(str(years.Vintages_Year) + "_retail_cose[]")[i]),
                                    Retail_Stock = str(request.POST.getlist(str(years.Vintages_Year) + "_retail_stock[]")[i]),
                                    Descount_Cost = str(request.POST.getlist(str(years.Vintages_Year) + "_descount_cose[]")[i]),
                                    Duty = str(request.POST.getlist(str(years.Vintages_Year) + "_duty[]")[i]),
                                    GST = str(request.POST.getlist(str(years.Vintages_Year) + "_GST[]")[i]),
                                    Bond_Cost = str(request.POST.getlist(str(years.Vintages_Year) + "_bond_cose[]")[i]),
                                    Bond_Stock = str(request.POST.getlist(str(years.Vintages_Year) + "_bond_stock[]")[i]),
                                    Bond_Descount_Cost = str(request.POST.getlist(str(years.Vintages_Year) + "_bond_descount_cost[]")[i]),
                                    Created_by = request.user,
                                    Updated_by = request.user
                                )
                                add_price.save()
                                i = i + 1
                                # ==================================================
                                if product_ins.LWineCode:
                                    lwine_code = str(product_ins.LWineCode)
                                    if years.Vintages_Year:
                                        year = str(years.Vintages_Year)
                                        set_lwine_code_with_year = lwine_code + year
                                        TEST_REVIEW = get_review(set_lwine_code_with_year)
                                # ==================================================
            # ========================== add Price CODE END================================
            messages.info(request, "Product add successfully.")
            if '_continue' in request.POST:
                return HttpResponseRedirect(reverse('admin_manage_products:update_products', args=(product_ins.Product_id,)))
            return HttpResponseRedirect(reverse('admin_manage_products:products'))
        else:
            return render(request, self.template_name, {'form': form,'Page_title':"Add Product"})

@method_decorator(login_required , name="dispatch")
class ManagProducFullImagtView(SuccessMessageMixin,generic.TemplateView):
    template_name ='admin/products/product_full_image.html'

    def get_context_data(self, *args,**kwargs):
        context  = super(ManagProducFullImagtView,self).get_context_data(*args,**kwargs)
        context['Page_title'] = "Manage Product"
        prodict_id = self.kwargs.get("prodict_id")
        get_product_ins = get_object_or_404(AwProducts, Product_id=prodict_id)
        image_list = []
        if AwProductImageFullView.objects.filter(Product=get_product_ins).exists():
            image_list = AwProductImageFullView.objects.filter(Product=get_product_ins).order_by('id')

        context['image_list'] = image_list
        context['product_ins'] = get_product_ins
        print(context)
        return context

    def post(self, request, *args, **kwargs):
        prodict_id = self.kwargs.get("prodict_id")
        get_product_ins = get_object_or_404(AwProducts, Product_id=prodict_id)
        if AwProductImageFullView.objects.filter(Product=get_product_ins).exists():
            AwProductImageFullView.objects.filter(Product=get_product_ins).delete()
            message_set = "Images update successfully."
        else:
            message_set = "Images add successfully."
        for item in request.FILES.getlist('images', False):
            add_image = AwProductImageFullView(Product=get_product_ins,Image=item)
            add_image.save()
        messages.info(request, message_set)
        return HttpResponseRedirect(reverse('admin_manage_products:products'))
        image_list = []
        if AwProductImageFullView.objects.filter(Product=get_product_ins).exists():
            image_list = AwProductImageFullView.objects.filter(Product=get_product_ins).order_by('id')
        return render(request, self.template_name, {'image_list': image_list, 'product_ins': get_product_ins})



@method_decorator(login_required , name="dispatch")
class ManageProductCostView(SuccessMessageMixin,generic.DetailView):
    template_name ='admin/products/product_cose.html'

    def get_context_data(self, *args,**kwargs):
        context  = super(ManageProductCostView,self).get_context_data(*args,**kwargs)
        context['Page_title'] = "Manage Product"
        prodict_id = self.kwargs.get("prodict_id")
        get_product_ins = get_object_or_404(AwProducts, Product_id=prodict_id)
        year_list = []
        if get_product_ins.Vintage.all():
            for items in get_product_ins.Vintage.all():
                year_list.append(items.Vintages_Year)
        context['year_list'] = year_list
        context['product_ins'] = get_product_ins
        print(context)
        return context

    def get_object(self, queryset=None):
        prodict_id = self.kwargs.get("prodict_id")
        get_product_ins =  get_object_or_404(AwProducts,Product_id=prodict_id)
        return AwProductPrice.objects.filter(Product=get_product_ins)




@method_decorator(login_required , name="dispatch")
class UpdateProductView(SuccessMessageMixin,generic.View):
    template_name = 'admin/products/product_edit.html'

    def get(self, request, *args, **kwargs):
        prodict_id = self.kwargs.get("prodict_id")
        get_product_ins = get_object_or_404(AwProducts, Product_id=prodict_id)
        form = AwProductsForm(instance=get_product_ins)
        get_product_image = None
        get_product_banner_image = None
        if AwProductImage.objects.filter(Product=get_product_ins).exists():
            get_product_image = AwProductImage.objects.filter(Product=get_product_ins)
            product_image = AwProductImage.objects.filter(Image_Type="Product_image").filter(Product=get_product_ins)
            add_image=""
            for data in product_image:
                add_image = data.Image
            AwProducts.objects.filter(id=get_product_ins.id).update(Product_image=add_image)

        if AwProductImage.objects.filter(Product=get_product_ins).filter(Image_Type="Product_Banner_image").exists():
            get_product_banner_image = get_object_or_404(AwProductImage,Product=get_product_ins,Image_Type="Product_Banner_image")
        get_price_and_cost = None
        if AwProductPrice.objects.filter(Product=get_product_ins):
            get_price_and_cost = AwProductPrice.objects.filter(Product=get_product_ins)
        year_list = []
        if get_product_ins.Vintage.all():
            for items in get_product_ins.Vintage.all():
                year_list.append(items.Vintages_Year)
        return render(request, self.template_name,{'year_list':year_list,'get_price_and_cost':get_price_and_cost,'get_product_banner_image':get_product_banner_image,'get_product_image':get_product_image,'get_product_ins':get_product_ins,'Page_title': "Edit Product", 'form':form})

    def post(self, request, *args, **kwargs):
        prodict_id = self.kwargs.get("prodict_id")
        get_product_ins = get_object_or_404(AwProducts, Product_id=prodict_id)
        form = AwProductsForm(request.POST,instance=get_product_ins)
        # return render(request, self.template_name, {'form_class': form, 'Page_title': "Add Product"})
        if form.is_valid():
            product_ins = form.save(commit=False)
            if request.POST["product_status"] == "Activate":
                product_ins.Status = True
            else:
                product_ins.Status = False
            product_ins.save()
            form.save_m2m()



            # ========================== add images CODE START================================

            AwProductImage.objects.filter(Product=product_ins).filter(Image_Type="Product_image").filter(~Q(id__in=request.POST.getlist('product_images_old[]'))).delete()

            if "product_images[]" in request.POST:
                if request.POST["product_images[]"]:
                    i = 0
                    for items in request.POST.getlist('product_images[]'):
                        format, imgstr = items.split(';base64,')
                        ext = format.split('/')[-1]
                        dateTimeObj = datetime.now()
                        today_date = date.today()
                        set_file_name = str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year) + "_" + str(dateTimeObj.microsecond)
                        file_name = set_file_name + "." + ext
                        data = ContentFile(base64.b64decode(imgstr), name=file_name)
                        # if i==0:
                        #     product_ins.Product_image.delete(save=False)
                        #     product_ins.Product_image = data
                        #     product_ins.save()
                        # else:
                        add_image = AwProductImage(Product=product_ins,Image_Type="Product_image",Image=data)
                        add_image.save()
                        i = i+1
            print(request.POST["product_banner_image"])
            if request.POST["product_banner_image"]:
                AwProductImage.objects.filter(Product=product_ins).filter(Image_Type='Product_Banner_image').delete()
                format_banner, imgstr_banner = request.POST["product_banner_image"].split(';base64,')
                ext_banner = format_banner.split('/')[-1]
                dateTimeObj_banner = datetime.now()
                today_date = date.today()
                set_file_name_banner = str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year) + "_" + str(dateTimeObj_banner.microsecond)
                file_name_banner = set_file_name_banner + "." + ext_banner
                data_banner = ContentFile(base64.b64decode(imgstr_banner), name=file_name_banner)
                add_image = AwProductImage(Product=product_ins, Image_Type="Product_Banner_image", Image=data_banner)
                add_image.save()


            if request.POST["product_thumbnail_image"]:
                format_thumbnail, imgstr_thumbnail = request.POST["product_thumbnail_image"].split(';base64,')
                ext_thumbnail = format_thumbnail.split('/')[-1]
                dateTimeObj_thumbnail = datetime.now()
                today_date = date.today()
                set_file_name_thumbnail = str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year) + "_" + str(dateTimeObj_thumbnail.microsecond)
                file_name_thumbnail = set_file_name_thumbnail + "." + ext_thumbnail
                data_thumbnail = ContentFile(base64.b64decode(imgstr_thumbnail), name=file_name_thumbnail)

                product_ins.Product_image.delete(save=False)
                product_ins.Product_image = data_thumbnail
                product_ins.save()
            # ========================== add images CODE END================================
            # # ========================== add Price CODE END================================
            if request.POST["all_remove_vintage_ids"]:
                get_all_removed_id = [int(x) for x in request.POST["all_remove_vintage_ids"].split(",")]
                AwProductPrice.objects.filter(id__in =get_all_removed_id).delete()
            if request.POST.getlist('Vintage'):
                get_vintage_year = AwVintages.objects.filter(id__in=request.POST.getlist('Vintage'))
                if get_vintage_year:
                    for years in get_vintage_year:
                        if str(years.Vintages_Year) + "_bottle[]" in request.POST:
                            i = 0
                            for items in request.POST.getlist(str(years.Vintages_Year) + "_bottle[]"):
                                if request.POST.getlist(str(years.Vintages_Year) + "_id[]")[i]:
                                    AwProductPrice.objects.filter(
                                        id=request.POST.getlist(str(years.Vintages_Year) + "_id[]")[i]).update(
                                        Product=product_ins,
                                        Vintage_Year=years,
                                        Bottle=str(request.POST.getlist(str(years.Vintages_Year) + "_bottle[]")[i]),
                                        Retail_Cost=str(
                                            request.POST.getlist(str(years.Vintages_Year) + "_retail_cose[]")[i]),
                                        Retail_Stock=str(
                                            request.POST.getlist(str(years.Vintages_Year) + "_retail_stock[]")[i]),
                                        Descount_Cost=str(
                                            request.POST.getlist(str(years.Vintages_Year) + "_descount_cose[]")[i]),
                                        Duty=str(request.POST.getlist(str(years.Vintages_Year) + "_duty[]")[i]),
                                        GST=str(request.POST.getlist(str(years.Vintages_Year) + "_GST[]")[i]),
                                        Bond_Cost=str(
                                            request.POST.getlist(str(years.Vintages_Year) + "_bond_cose[]")[i]),
                                        Bond_Stock=str(
                                            request.POST.getlist(str(years.Vintages_Year) + "_bond_stock[]")[i]),
                                        Bond_Descount_Cost=str(
                                            request.POST.getlist(str(years.Vintages_Year) + "_bond_descount_cost[]")[
                                                i]),
                                        Created_by=request.user,
                                        Updated_by=request.user)
                                    # ==================================================
                                    if product_ins.LWineCode:
                                        lwine_code = str(product_ins.LWineCode)
                                        if years.Vintages_Year:
                                            year = str(years.Vintages_Year)
                                            set_lwine_code_with_year = lwine_code + year
                                            TEST_REVIEW = get_review(set_lwine_code_with_year)
                                    # ==================================================

                                else:
                                    add_price = AwProductPrice(
                                        Product=product_ins,
                                        Vintage_Year=years,
                                        Bottle=str(request.POST.getlist(str(years.Vintages_Year) + "_bottle[]")[i]),
                                        Retail_Cost=str(
                                            request.POST.getlist(str(years.Vintages_Year) + "_retail_cose[]")[i]),
                                        Retail_Stock=str(
                                            request.POST.getlist(str(years.Vintages_Year) + "_retail_stock[]")[i]),
                                        Descount_Cost=str(
                                            request.POST.getlist(str(years.Vintages_Year) + "_descount_cose[]")[i]),
                                        Duty=str(request.POST.getlist(str(years.Vintages_Year) + "_duty[]")[i]),
                                        GST=str(request.POST.getlist(str(years.Vintages_Year) + "_GST[]")[i]),
                                        Bond_Cost=str(
                                            request.POST.getlist(str(years.Vintages_Year) + "_bond_cose[]")[i]),
                                        Bond_Stock=str(
                                            request.POST.getlist(str(years.Vintages_Year) + "_bond_stock[]")[i]),
                                        Bond_Descount_Cost=str(
                                            request.POST.getlist(str(years.Vintages_Year) + "_bond_descount_cost[]")[
                                                i]),
                                        Created_by=request.user,
                                        Updated_by=request.user
                                    )
                                    add_price.save()
                                    # ==================================================
                                    if product_ins.LWineCode:
                                        lwine_code = str(product_ins.LWineCode)
                                        if years.Vintages_Year:
                                            year = str(years.Vintages_Year)
                                            set_lwine_code_with_year = lwine_code+year
                                            TEST_REVIEW = get_review(set_lwine_code_with_year)
                                    # ==================================================
                                i = i + 1
            # ========================== add Price CODE END================================
            messages.info(request, "Product update successfully.")
            if '_continue' in request.POST:
                return HttpResponseRedirect(reverse('admin_manage_products:update_products', args=(prodict_id,)))
            return HttpResponseRedirect(reverse('admin_manage_products:products'))
        else:
            get_product_image = None
            get_product_banner_image = None
            if AwProductImage.objects.filter(Product=get_product_ins).exists():
                get_product_image = AwProductImage.objects.filter(Product=get_product_ins)
            if AwProductImage.objects.filter(Product=get_product_ins).filter(
                    Image_Type="Product_Banner_image").exists():
                get_product_banner_image = get_object_or_404(AwProductImage, Product=get_product_ins,
                                                             Image_Type="Product_Banner_image")
            get_price_and_cost = None
            if AwProductPrice.objects.filter(Product=get_product_ins):
                get_price_and_cost = AwProductPrice.objects.filter(Product=get_product_ins)
            year_list = []
            if get_product_ins.Vintage.all():
                for items in get_product_ins.Vintage.all():
                    year_list.append(items.Vintages_Year)
            return render(request, self.template_name, {'year_list':year_list,'get_price_and_cost':get_price_and_cost,'get_product_banner_image':get_product_banner_image,'get_product_image':get_product_image,'get_product_ins':get_product_ins,'Page_title': "Edit Product",'form':form})



class ProductsDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = AwProducts
    template_name = 'admin/products/delete.html'
    success_url = reverse_lazy('admin_manage_products:products')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Delete Product"
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Product remove successfully."


