from django.shortcuts import get_object_or_404
from rest_framework.generics import (CreateAPIView, 
                                     DestroyAPIView, 
                                     ListAPIView, 
                                     ListCreateAPIView, 
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.db.models import Q, Count
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.exceptions import ValidationError, BadRequest
import json
from hificom.models import (Carousel, Cart, Category,
                            CategoryGroup, Coupon, KeyFeature,
                            Order, Product, ProductCollection,
                            Question, Review, SpecificationTable, FeedBack)

from .serializer import (CarouselSerializer, CategoryDetailSerializer, CategoryGroupSerializer,
                         CategorySerializer, KeyFeatureSerializer, OrderSerializer, OrderDetailSerializer,
                         ProductBasicSerializer, ProductCollectionSerializer, ProductCreateSerializer,
                         ProductDetailSerializer, ProductSemiDetailSerializer, QuestionSerializer,
                         SpecTableSerializer, ReviewSerializer, CouponSerializer,
                         WishlistSerializer, FeedbackSerializer)

from .permission import IsAdminOrReadOnly, IsAdmin
from .pagination import (OrderPagination, 
                        ProductsPagination, 
                        QuestionsReviewsPagination,
                        FeedbackPagination)
from . import utils
from ..models import feedback_status_options
from rest_framework.exceptions import ValidationError

User = get_user_model()


@api_view()
def user_homepage(request):
    data = {
        'carousels': CarouselSerializer(
            Carousel.objects.filter(active=True),
            many=True,
            context={'request': request}
        ).data,
        'collections': ProductCollectionSerializer(
            ProductCollection.objects.all(),
            many=True,
            context={'request': request}
        ).data,
    }
    return Response(data)

class ProductCollectionsView(ListAPIView):
    serializer_class = ProductCollectionSerializer
    queryset = ProductCollection.objects.all()

class CategoriesView(ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        cat_type = self.request.GET.get('type', 'all')
        parent= self.request.GET.get('parent', 'null')
        parent_in_tree_of = self.request.GET.get('treeof', 'null')
        categories = Category.objects.all()
        if cat_type != 'all':
            categories = categories.filter(cat_type=cat_type)
        if parent == 'null' and parent_in_tree_of == 'null':
            categories = categories.filter(parent=None)
        elif parent == 'null' and parent_in_tree_of != 'null':
            tree_of = get_object_or_404(
                Category,
                Q(pk=parent_in_tree_of) | Q(slug=parent_in_tree_of) if parent_in_tree_of.isdigit() 
                else Q(slug=parent_in_tree_of)
            )
            categories = categories.filter(parent__in=tree_of.category_tree)
        elif parent != 'null' and parent != 'all':
            categories = categories.filter(
                Q(parent__pk=parent) | Q(parent__slug=parent) if parent.isdigit()
                else Q(parent__slug=parent)
            )
        return categories


class CategoryGroupsView(ListAPIView):
    serializer_class = CategoryGroupSerializer

    def get_queryset(self):
        root_cat = utils.get_category_from_identifier(self.kwargs.get('identifier'))
        return CategoryGroup.objects.filter(root__in=root_cat.category_tree)


class ViewCategory(RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.all()

    def get_object(self):
        return utils.get_category_from_identifier(self.kwargs.get('identifier'))


class CategorTablesView(ListAPIView):
    serializer_class = SpecTableSerializer

    def get_object(self):
        return utils.get_category_from_identifier(self.kwargs.get('identifier'))
    
    def get_queryset(self):
        category = self.get_object()
        if self.request.GET.get('tree'):
            return SpecificationTable.objects.filter(category__in=category.category_tree)
        else:
            category.specificationtable_set.all()


class CategoryUnpaginatedProductsView(ListAPIView):
    serializer_class = ProductBasicSerializer

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs.get('slug'))


class CategoryProductsView(CategoryUnpaginatedProductsView):
    pagination_class = ProductsPagination


class TaggedProductsUnpaginatedView(ListAPIView):
    serializer_class = ProductBasicSerializer
    
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Product.objects.filter(Q(category__slug=slug) | Q(tags__slug=slug)).distinct()


class TaggedProductsView(TaggedProductsUnpaginatedView):
    pagination_class = ProductsPagination


class SearchProduct(ListAPIView):
    serializer_class = ProductBasicSerializer

    def get_queryset(self):
        query = self.request.GET.get('query')
        products = Product.objects.filter(Q(title__icontains=query))
        return products


class AllProductsSemiDetailView(ListAPIView):
    serializer_class = ProductSemiDetailSerializer
    pagination_class = ProductsPagination
    
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return utils.filter_products(slug, self.request)


class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    lookup_field = 'slug'


class ProductKeyFeaturesView(ListAPIView):
    serializer_class = KeyFeatureSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return KeyFeature.objects.filter(product__slug=slug)
    

class RelatedProductsView(ListAPIView):
    serializer_class = ProductBasicSerializer
    
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        limit = self.request.GET.get('limit', '10')
        if limit.isdigit():
            limit = int(limit)
        prod = get_object_or_404(Product, slug=slug)
        all_related_products = Product.objects.filter(tags__in=prod.tags.all()).exclude(pk=prod.id)
        updated_qs = all_related_products.annotate(
            num_matching_tags_count = Count('tags', filter=Q(tags__in=prod.tags.all()))
        ).order_by('-num_matching_tags_count')[:limit]
        return updated_qs


class ProductQuestions(ListCreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = QuestionsReviewsPagination

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Product, slug=slug)
    
    def get_queryset(self):
        product = self.get_object()
        return product.question_set.all()
    
    def perform_create(self, serializer):
        serializer.save(
            product = self.get_object(),
            account = self.request.user
        )


class ProductReviews(ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    pagination_class = QuestionsReviewsPagination

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Product, slug=slug)
    
    def get_queryset(self):
        product = self.get_object()
        return product.review_set.all()
    
    def perform_create(self, serializer):
        serializer.save(
            product = self.get_object(),
            account = self.request.user
        )

class OrderList(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAdmin]
    pagination_class = OrderPagination

    def get_queryset(self):
        orders = Order.objects.all().order_by('id')
        status = self.request.GET.get('status')
        excludestatus = self.request.GET.get('excludestatus')
        if status:
            orders = orders.filter(status = status)
        if excludestatus:
            orders = orders.filter(status != excludestatus)
        if self.request.GET.get('running'):
            orders = orders.filter(status__in=['pending', 'processing', 'shipped'])
        return orders

class MyOrderList(OrderList):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-added_at')


class OrderDetail(RetrieveAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = []
    queryset = Order.objects.all()
    
    def get_object(self):
        oid = self.kwargs.get('oid')
        return get_object_or_404(Order, oid=oid) 

class DeleteProduct(DestroyAPIView):
    serializer_class = ProductBasicSerializer
    queryset = Product.objects.all()
    permission_classes=[IsAdmin]


class ConfirmOrder(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        cart = get_object_or_404(Cart, cartid=data.pop('cartid'))
        if not cart.check_all_products_in_stock():
            return Response(
                {'detail': 'Some products in cart are out of stock'},
                status=status.HTTP_400_BAD_REQUEST
            )
        item_count, payable = cart.cart_total()
        payable += utils.get_shipping_charges(item_count, data['location'])
        coupon_code = data.get('coupon')
        if coupon := Coupon.objects.filter(code=coupon_code).first():
            payable -= utils.get_coupon_discount_amount(cart, coupon)
            data['coupon'] = coupon.id
        data['payable'] = payable
        data['cart'] = cart.id
        if request.user.is_authenticated:
            data['user'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        utils.update_cart_checked_out(cart, request)
        return Response(serializer.data)


class Carousels(ListAPIView):
    serializer_class = CarouselSerializer
    permission_classes = [IsAdmin]
    queryset = Carousel.objects.all()
    

class CouponsView(ListCreateAPIView):
    serializer_class = CouponSerializer
    permission_classes = [IsAdmin]
    queryset = Coupon.objects.all()

@api_view(['POST'])
@permission_classes([IsAdmin])
def add_carousel(request):
    data = json.loads(request.data['json'])
    banner = request.FILES.get('banner')
    if not banner:
        return Response({'detail': 'No banner image provided'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        banner = utils.crop_to_1920x1080(banner)
    except Exception as e:
        return Response({'detail': f'Error processing image: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = CarouselSerializer(data=data)
    if serializer.is_valid():
        carousel = serializer.save()
        carousel.banner = banner
        carousel.save()
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response('added')

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
        try:
            serializer.save()
        except Exception as e:
            return Response({'detail': f'Cannot add product. Error: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response('added')


@api_view(['POST'])
@permission_classes([IsAdmin])
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    data = json.loads(request.data['json'])
    data['prev_images'] = data.pop('images')
    data['images'] = request.FILES.getlist('new_images')
    serializer = ProductCreateSerializer(product, data=data)
    if serializer.is_valid():
        try:
            serializer.save()
        except Exception as e:
            return Response({'detail': f'Cannot edit product. Error: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'category': product.category.slug})


@api_view(['POST'])
@permission_classes([IsAdmin])
def alter_stock_status(request, pk):
    product = get_object_or_404(Product, pk=pk)
    stock_status = request.data.get('in_stock')
    if type(stock_status) == bool:
        product.in_stock = stock_status
        product.save()
        return Response({'in_stock': product.in_stock})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view()
@permission_classes([IsAdmin])
def dashboard_stats(request):
    data = {
        'num_products': Product.objects.count(),
        'num_users': User.objects.count(),
        'num_orders': Order.objects.filter(status__in=['pending', 'processing', 'shipped']).count(),
        'num_pending_feedbacks': FeedBack.objects.filter(status='pending').count(),
    }
    return Response(data)


@api_view(['POST'])
def get_cart_products(request):
    cart = utils.get_cart(request)
    cartinfo = request.data.get('cartinfo')
    utils.update_cart(cart, cartinfo)
    products = [cartprod.product for cartprod in cart.cartproduct_set.all()]
    data = {'cartid': cart.cartid, 'prod_data': []}
    if products:
        serializer = ProductBasicSerializer(products, many=True, context={'request': request})
        data['prod_data'] = serializer.data
    data['total_items'], data['total_amount'] = cart.cart_total()
    data['all_in_stock'] = cart.check_all_products_in_stock()
    return Response(data)


@api_view(['POST'])
def apply_coupon(request):
    coupon = get_object_or_404(Coupon, code=request.data.get('coupon'))
    cart = get_object_or_404(Cart, cartid=request.data.get('cartid'))
    try:
        discount_amount = utils.get_coupon_discount_amount(cart, coupon)
    except ValidationError as e:
        return Response({'detail': e.message}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'discount': discount_amount})


@api_view()
def initiate_wishlist(request):
    wlist = utils.perform_wishlist_initiation(request)
    return Response(WishlistSerializer(wlist, context={'request': request}).data)

@api_view(['POST'])
def sync_wishlist(request):
    wlist = utils.perform_wishlist_sync(request)
    return Response(WishlistSerializer(wlist, context={'request': request}).data)


@api_view(['POST'])
@permission_classes([IsAdmin])
def alter_order_status(request, oid):
    order = get_object_or_404(Order, oid=oid)
    try:
        utils.change_order_status(order)
    except Exception as e:
        return Response(
            {'detail': str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )
    return Response({'info': f'Status changed to {order.status.title()}'})


@api_view(['POST'])
@permission_classes([IsAdmin])
def cancel_order(request, oid):
    order = get_object_or_404(Order, oid=oid)
    try:
        utils.cancel_order(order)
    except Exception as e:
        return Response(
            {'detail': str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )
    return Response({'info': 'Order cancelled'})


@api_view(['POST'])
@permission_classes([IsAdmin])
def undo_alter_status(request, oid):
    order = get_object_or_404(Order, oid=oid)
    try:
        utils.perform_undo_status_change(order)
    except Exception as e:
        return Response(
            {'detail': str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )
    return Response({'info': f'Status changed back to {order.status.title()}'})


@api_view(['POST'])
@permission_classes([IsAdmin])
def modify_carousel(request):
    allowed_commands = ['toggle_active', 'edit', 'delete']
    command = request.data.get('command')
    if command not in allowed_commands:
        return Response(
            {'detail': 'No operations can be performed'},
            status=status.HTTP_400_BAD_REQUEST
        )
    carousel = get_object_or_404(Carousel, pk=request.data.get('id'))
    if command == 'toggle_active':
        # dont allow if its the only active carousel
        if carousel.active and Carousel.objects.filter(active=True).count() == 1:
            return Response(
                {'detail': 'At least one carousel must be active'},
                status=status.HTTP_400_BAD_REQUEST
            )
        carousel.active = not carousel.active
        carousel.save()
    elif command == 'edit':
        serializer = CarouselSerializer(carousel, data=request.data.get('data'))
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif command == 'delete':
        carousel.delete()
    return Response('done')


@api_view(['POST'])
@permission_classes([IsAdmin])
def reorder_carousels(request):
    try:
        utils.reorder_carousels(request.data.get('id_order', []))
    except Exception as e:
        return Response(
            {'detail': str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )
    return Response('Reordered')

@api_view()
@permission_classes([IsAdmin])
def category_graph(request):
    categories = Category.objects.filter(cat_type__in=['general', 'brand', 'series', 'feature'])
    nodes = []
    edges = []
    
    for category in categories:
        nodes.append({
            "id": category.id,
            "label": category.title,
            # Add extra fields like description if needed
        })
        if category.parent:
            edges.append({
                "from": category.parent.id,
                "to": category.id
            })
    
    return Response({"nodes": nodes, "edges": edges})


@api_view(['POST'])
@permission_classes([IsAdmin])
def remove_collection_product(request):
    collection = get_object_or_404(ProductCollection, pk=request.data.get('collection'))
    product = get_object_or_404(Product, pk=request.data.get('product'))
    collection.products.remove(product)
    return Response('Removed')


@api_view(['POST'])
@permission_classes([IsAdmin])
def add_collection_product(request):
    collection = get_object_or_404(ProductCollection, pk=request.data.get('collection'))
    product = get_object_or_404(Product, pk=request.data.get('product'))
    collection.products.add(product)
    return Response('Added')


@api_view(['POST'])
@permission_classes([IsAdmin])
def delete_coupon(request):
    coupon = get_object_or_404(Coupon, pk=request.data.get('id'))
    coupon.delete()
    return Response('Deleted')


class FeedbackList(ListAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = FeedbackPagination
    
    def get_queryset(self):
        if self.request.user.is_staff:
            status = self.request.GET.get('status', 'all')
            feedbacks = FeedBack.objects.all()
            if status in [i[0] for i in feedback_status_options]:
                feedbacks = feedbacks.filter(status=status)
            return feedbacks
        return FeedBack.objects.filter(user=self.request.user)

class FeedbackDetail(RetrieveAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]
    queryset = FeedBack.objects.all()

    def get_object(self):
        feedback = get_object_or_404(FeedBack, pk=self.kwargs.get('pk'))
        if not self.request.user.is_staff and feedback.user != self.request.user:
            raise ValidationError('You do not have permission to view this feedback')
        return feedback


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_feedback(request):
    serializer = FeedbackSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response('Feedback submitted')

@api_view(['POST'])
@permission_classes([IsAdmin])
def reply_feedback(request, pk):
    feedback = get_object_or_404(FeedBack, pk=pk)
    feedback.reply_text = request.data.get('reply_text')
    feedback.status = 'replied'
    feedback.replied_at = timezone.now()
    feedback.replied_by = request.user
    feedback.save()
    return Response('Replied')


@api_view(['POST'])
@permission_classes([IsAdmin])
def delete_category(request, identifier):
    cat = get_object_or_404(Category, slug=identifier)
    if not cat.manual:
        return Response({'detail': 'Cannot delete yaml generated categories'}, status=status.HTTP_400_BAD_REQUEST)
    cat.delete()
    return Response('Deleted')