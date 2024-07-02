from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from hificom.models import Category
from .serializer import CategorySerializer, CategoryWithChildSerializer
from .permission import IsAdminOrReadOnly

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
    
    def create(self, request, *args, **kwargs):
        print(request.data, flush=1)
        return super().create(request, *args, **kwargs)

 
class ViewCategory(RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryWithChildSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.all()

    def get_object(self):
        return Category.objects.get(slug=self.kwargs.get('slug'))
