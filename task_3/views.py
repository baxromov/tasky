from django.http import FileResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.utils.redis import cache_response
from task_3 import models, serializers, filters


class ProductModelViewSet(ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductModelSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = filters.ProductFilterSet
    search_fields = [
        'name',
        'price',
        'description',
    ]

    # Cache the response
    @cache_response('product-cache', expiration=12)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def upload_file(self, request, pk=None):
        product = self.get_object()
        file = request.FILES.get('file')

        if file:
            product.file = file
            product.save()
            return Response({'message': 'File uploaded successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No file found in the request.'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def download_file(self, request, pk=None):
        product = self.get_object()
        file = product.file

        if file:
            file_path = file.path
            return FileResponse(open(file_path, 'rb'), as_attachment=True)
        else:
            return Response({'message': 'No file available for download.'}, status=status.HTTP_404_NOT_FOUND)
