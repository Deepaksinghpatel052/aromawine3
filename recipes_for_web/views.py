from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from manage_wine_recipes.models import AwWineRecipes
from django.contrib.messages.views import SuccessMessageMixin
from django.template.defaulttags import register
from admin_manage_products.models import AwProductPrice,AwProducts
from django.db.models import Q






# Create your views here.
class RecipesView(SuccessMessageMixin,generic.ListView):
    model = AwWineRecipes
    template_name = 'web/recipes/recipes.html'
    queryset = None
    paginate_by = 2

    def get_queryset(self, **kwargs):

        filters = None
        filters = Q(Status=True)

        # ======================================producers FLTER START======================
        if 'event-type' in self.request.GET:
            filters = filters & Q(Event_Type__Slug__in=self.request.GET.getlist('event-type'))
        # ======================================producers FLTER END======================

        set_filters = "-id"
        if "short-by" in self.request.GET:
            if self.request.GET['short-by'] == "asc":
                set_filters = 'id'
            if self.request.GET['short-by'] == "name":
                set_filters = 'Name'


        get_data = AwWineRecipes.objects.filter(filters).order_by(set_filters)
        return get_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Recipes"

        if 'short-by' in self.request.GET:
            context['short_by_set'] = self.request.GET['short-by']

        # event_type = AwEventType.objects.all().order_by("-id")
        # context['event_type'] = event_type

        # ======================================bottel-size FLTER START======================
        context['event-type'] = []
        if 'event-type' in self.request.GET:
            context['event_type_set'] = self.request.GET.getlist('event-type')
        # ======================================bottel-size FLTER END======================
        return context



class QuickViewRecipe(generic.DetailView):
    template_name = "web/recipes/quick_detail_recipe.html"
    model = AwWineRecipes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context



class DetailView(generic.TemplateView):
    template_name = "web/recipes/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_id = self.kwargs.get("recipe_id")
        recipe_slug = self.kwargs.get("recipe_slug")
        recipe_data = None
        if AwWineRecipes.objects.filter(id=recipe_id).exists():
            recipe_data = get_object_or_404(AwWineRecipes,id=recipe_id)
        context['Page_title'] = recipe_slug
        context['recipe_data'] = recipe_data

        if AwProducts.objects.filter(Status=True).exists():
            get_trending_wines = AwProducts.objects.filter(Status=True)
        context['trending_wines'] = get_trending_wines
        return context
