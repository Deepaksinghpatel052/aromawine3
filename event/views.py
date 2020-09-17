from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from manage_event.models import AwEvent,AwEventType
from django.contrib.messages.views import SuccessMessageMixin
from django.template.defaulttags import register
from admin_manage_products.models import AwProductPrice,AwProducts
from django.db.models import Q
from django import template
from django.template.loader import render_to_string



@register.filter(name='times_loop')
def times_loop(number):
    return option


@register.filter(name='get_page_link')
def get_page_link(number):
    option = []
    for i in range(0,number):
        option.append(str(i+1))
    return render_to_string('web/event/forloop.html',{"option":option})


# Create your views here.
class EventView(SuccessMessageMixin,generic.ListView):
    model = AwEvent
    template_name = 'web/event/events.html'
    queryset = None
    paginate_by = 7

    def get_queryset(self, **kwargs):

        filters = None
        filters = Q(Status=True)

        # ======================================producers FLTER START======================
        if 'event-type' in self.request.GET:
            filters = filters & Q(Event_Type__Slug__in=self.request.GET.getlist('event-type'))
        # ======================================producers FLTER END======================

        set_filters = "-id"
        if "short-by" in self.request.GET:
            if self.request.GET['short-by'] == "price":
                set_filters = 'ticket_price'
            if self.request.GET['short-by'] == "name":
                set_filters = 'Event_name'


        get_data = AwEvent.objects.filter(filters).order_by(set_filters)
        return get_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Event"
        get_event = None
        if AwEvent.objects.filter(Status=True).exists():
            get_event = AwEvent.objects.filter(Status=True).order_by("-id")
        context['get_event'] = get_event

        if 'short-by' in self.request.GET:
            context['short_by_set'] = self.request.GET['short-by']

        event_type = AwEventType.objects.all().order_by("-id")
        context['event_type'] = event_type

        # ======================================bottel-size FLTER START======================
        context['event-type'] = []
        if 'event-type' in self.request.GET:
            context['event_type_set'] = self.request.GET.getlist('event-type')
        # ======================================bottel-size FLTER END======================
        return context



class QuickVuewEvent(generic.DetailView):
    template_name = "web/event/quick_detail_event.html"
    model = AwEvent

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        # if AwEvent.objects.filter(id=self).filter(Vintage_Year=context['object'].Vintage_Year).exists():
        #     get_all_bottel_set_of_this_year = AwProductPrice.objects.filter(Product=context['object'].Product).filter(Vintage_Year=context['object'].Vintage_Year)
        # context['get_all_bottel_set_of_this_year'] = get_all_bottel_set_of_this_year
        return context



class DetailView(generic.TemplateView):
    template_name = "web/event/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event_id = self.kwargs.get("event_id")
        event_slug = self.kwargs.get("event_slug")
        event_data = None
        if AwEvent.objects.filter(id=event_id).exists():
            event_data = get_object_or_404(AwEvent,id=event_id)
        context['Page_title'] = event_slug
        context['event_data'] = event_data

        if AwProducts.objects.filter(Status=True).exists():
            get_trending_wines = AwProducts.objects.filter(Status=True)
        context['trending_wines'] = get_trending_wines
        return context