from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
import json
from hificom.models import Category, Product
from .serializer import (CategorySerializer, 
                         CategoryDetailSerializer, 
                         ProductImageSerializer,
                         ProductCreateSerializer)
from .permission import IsAdminOrReadOnly
from . import utils

class CategoriesView(ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        cat_type = self.request.GET.get('type', 'all')
        parent= self.request.GET.get('parent', 'null')
        categories = Category.objects.all()
        if cat_type != 'all':
            categories = categories.filter(cat_type=cat_type)
        if parent == 'null':
            categories = categories.filter(parent=None)
        elif parent != 'null' and  parent.isdigit():
            parent_id = int(parent)
            categories = categories.filter(parent__id=parent_id)
        return categories

 
class ViewCategory(RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.all()

    def get_object(self):
        return Category.objects.get(slug=self.kwargs.get('slug'))


@api_view(['POST'])
@permission_classes([IsAdminOrReadOnly])
def update_tables(request, slug):
    cat = get_object_or_404(Category, slug=slug)
    try:
        utils.update_cat_tables(cat, request.data)
    except Exception as e:
        return Response({'detail': f'Error while updating: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
    return Response('Updated')

@api_view(['POST'])
@permission_classes([IsAdminOrReadOnly])
def add_product(request, slug):
    data = json.loads(request.data['json'])
    data['images'] = request.FILES.getlist('images')
    serializer = ProductCreateSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response('testing')