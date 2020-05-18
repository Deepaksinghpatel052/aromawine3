from admin_manage_products.models import AwProductPrice
import django_filters

class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = AwProductPrice
        fields = ['Product__Color', ]
