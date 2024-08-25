from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class ProductsPagination(PageNumberPagination):
    page_size = 21

    def get_paginated_response(self, data):
        return Response({
            'current_page': self.page.number,
            'total_pages': self.page.paginator.num_pages,
            'per_page': self.page.paginator.per_page,
            'results': data,
        })