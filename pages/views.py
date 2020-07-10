from django.shortcuts import render,get_object_or_404
from django.views import generic
from admin_manage_grape.models import AwGrape
from django.db.models import Max,Min,Count
from admin_manage_producer.models import AwProducers
from admin_manage_region.models import AwRegion
from admin_manage_products.models import AwProductPrice,AwProducts,AwProductImage,AwWineType
from admin_manage_country.models import AwCountry
# Create your views here.
class PageContentView(generic.TemplateView):
	template_name = "web/page/page_content.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		page_content = None
		page_title = None
		page_banner_image = None
		Products = None
		type = self.kwargs.get("type")
		page_slug = self.kwargs.get("page_slug")
		# ======================================  FOR grape start ==================================
		if type == 'grape':
			if AwGrape.objects.filter(Slug=page_slug).exists():
				page_content =  get_object_or_404(AwGrape,Slug=page_slug)
				page_title = page_content.Grape_Name
				page_banner_image = page_content.Grape_Image
				if page_content.Grape_banner_Image:
					page_banner_image = page_content.Grape_banner_Image
				if AwProductPrice.objects.filter(Product__Grape__Slug=page_slug).exists():
					Products = AwProductPrice.objects.filter(Product__Grape__Slug=page_slug).annotate(replies=Count('Vintage_Year') - 1)
		# ======================================  FOR grape end ==================================

		# ======================================  FOR AwProducers start ==================================
		if type == 'producer':
			if AwProducers.objects.filter(Slug=page_slug).exists():
				page_content =  get_object_or_404(AwProducers,Slug=page_slug)
				page_title = page_content.Winnery_Name
				page_banner_image = page_content.Producer_Image
				if page_content.Producer_Banner_Image:
					page_banner_image = page_content.Producer_Banner_Image
				if AwProductPrice.objects.filter(Product__Producer__Slug=page_slug).exists():
					Products = AwProductPrice.objects.filter(Product__Producer__Slug=page_slug).annotate(replies=Count('Vintage_Year') - 1)
		# ======================================  FOR grape end ==================================
		# ======================================  FOR AwRegion start ==================================
		if type == 'region':
			if AwRegion.objects.filter(Slug=page_slug).exists():
				page_content = get_object_or_404(AwRegion, Slug=page_slug)
				page_title = page_content.Region_Name
				page_banner_image = page_content.Region_Image
				if page_content.Region_banner_Image:
					page_banner_image = page_content.Region_banner_Image
				if AwProductPrice.objects.filter(Product__Regions__Slug=page_slug).exists():
					Products = AwProductPrice.objects.filter(Product__Regions__Slug=page_slug).annotate(
						replies=Count('Vintage_Year') - 1)
		# ======================================  FOR grape end ==================================

		# ======================================  FOR AwRegion start ==================================
		if type == 'region':
			if AwRegion.objects.filter(Slug=page_slug).exists():
				page_content = get_object_or_404(AwRegion, Slug=page_slug)
				page_title = page_content.Region_Name
				page_banner_image = page_content.Region_Image
				if page_content.Region_banner_Image:
					page_banner_image = page_content.Region_banner_Image
				if AwProductPrice.objects.filter(Product__Regions__Slug=page_slug).exists():
					Products = AwProductPrice.objects.filter(Product__Regions__Slug=page_slug).annotate(
						replies=Count('Vintage_Year') - 1)
		# ======================================  FOR grape end ==================================

		# ======================================  FOR AwCountry start ==================================
		if type == 'country':
			if AwCountry.objects.filter(Slug=page_slug).exists():
				page_content = get_object_or_404(AwCountry, Slug=page_slug)
				page_title = page_content.Country_Name
				page_banner_image = page_content.Country_Image
				if page_content.Country_Banner_Image:
					page_banner_image = page_content.Country_Banner_Image
				if AwProductPrice.objects.filter(Product__Country__Slug=page_slug).exists():
					Products = AwProductPrice.objects.filter(Product__Country__Slug=page_slug).annotate(
						replies=Count('Vintage_Year') - 1)
		# ======================================  FOR country end ==================================

		context['page_content'] = page_content
		context['Page_title'] = page_title
		context['page_banner_image'] = page_banner_image
		context['Products'] = Products
		context['type'] = type
		return context