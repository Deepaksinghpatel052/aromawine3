from django.shortcuts import render,get_object_or_404
from django.views import generic
from admin_manage_grape.models import AwGrape
from django.db.models import Max,Min,Count
from admin_manage_producer.models import AwProducers
from admin_manage_region.models import AwRegion
from admin_manage_products.models import AwProductPrice,AwProducts,AwProductImage,AwWineType
from admin_manage_country.models import AwCountry
from admin_manage_color.models import AwColor
from admin_manage_appellation.models import AwAppellation
from admin_manage_size.models import AwSize
from admin_manage_classification.models import AwClassification
from home.models import AwCmsPaage
from admin_manage_Vintages.models import AwVintages
from admin_manage_Vintages.models import AwVintages
from admin_manage_varietals.models import AwVarietals
from admin_manage_dinner.models import AwDinner
from admin_manag_wine_testing.models import AwTesting
# Create your views here.
class PageContentView(generic.TemplateView):
	template_name = "web/page/page_content.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		page_content = None
		page_title = self.kwargs.get("type")
		page_title_show = self.kwargs.get("type")
		page_banner_image = None
		page_info_data_set = None
		Products = None
		type = self.kwargs.get("type")
		page_slug = self.kwargs.get("page_slug")
		# ======================================  FOR grape start ==================================
		if type == 'grape':
			if AwGrape.objects.filter(Status=True).exists():
				page_content =  AwGrape.objects.filter(Status=True)
		# ======================================  FOR grape end ==================================

		# ======================================  FOR AwProducers start ==================================
		if type == 'producer':
			if AwProducers.objects.filter(Status=True).exists():
				page_content =  AwProducers.objects.filter(Status=True)
		# ======================================  FOR grape end ==================================
		# ======================================  FOR AwRegion start ==================================
		if type == 'region':
			if AwRegion.objects.filter(Status=True).exists():
				page_content = AwRegion.objects.filter(Status=True)
		# ======================================  FOR grape end ==================================

		# ======================================  FOR AwCountry start ==================================
		if type == 'country':
			if AwCountry.objects.filter(Status=True).exists():
				page_content = AwCountry.objects.filter(Status=True)
		# ======================================  FOR country end ==================================
		# ======================================  FOR AwDinner start ==================================
		if type == 'dinner':
			if AwDinner.objects.filter(Status=True).exists():
				page_content = AwDinner.objects.filter(Status=True)
		# ======================================  FOR AwDinner end ==================================

		# ======================================  FOR AwTesting start ==================================
		if type == 'wine-testing':
			if AwTesting.objects.filter(Status=True).exists():
				page_content = AwTesting.objects.filter(Status=True)
		# ======================================  FOR AwTesting end ==================================
		if AwCmsPaage.objects.filter(Slug=type).exists():
			page_info = get_object_or_404(AwCmsPaage,Slug=type)
			page_title_show = page_info.Title
			page_banner_image = page_info.Background_Image.url
			page_info_data_set = page_info.description

		context['page_content'] = page_content
		context['Page_title'] = page_title
		context['page_title_show'] = page_title_show
		context['page_banner_image'] = page_banner_image
		context['page_info_data_set'] = page_info_data_set

		return context