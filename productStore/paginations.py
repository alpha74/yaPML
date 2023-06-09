from rest_framework.pagination import PageNumberPagination

# Page size is 3
class ProductListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100