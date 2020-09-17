from rest_framework.pagination import LimitOffsetPagination , PageNumberPagination

class ProductLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10

class PrtoductPageNumberPagination(PageNumberPagination):
    page_size = 10