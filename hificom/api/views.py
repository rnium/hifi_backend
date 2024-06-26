from rest_framework.generics import ListCreateAPIView
from hificom.models import Category
from .serializer import CategorySerializer
from .permission import IsAdminOrReadOnly

class CategoryView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminOrReadOnly]