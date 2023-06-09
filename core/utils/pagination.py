from rest_framework import pagination


class PageNumberPagination(pagination.PageNumberPagination):
    page_size_query_param = 'limit'

    def paginate_queryset(self, queryset, request, view=None):
        return super().paginate_queryset(queryset, request, view)
