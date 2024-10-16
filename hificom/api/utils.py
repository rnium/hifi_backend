from datetime import timedelta
from typing import Dict, List
from hificom.models import (Category, SpecificationTable, 
                            Specification, ProductSpec, ProductImage, KeyFeature, Order, OrderStatusTimestamp,
                            TitleAlias, Product, Cart, CartProduct, Coupon, WishList)
from django.db.models import Model, Count, Q
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.conf import settings


def delete_db_objects(model: Model, ids: List[int]):
    if not ids:
        return
    qs = model.objects.filter(id__in=ids)
    qs.delete()


def get_category_from_identifier(identifier):
    return get_object_or_404(Category, Q(id=identifier) if identifier.isdigit() else Q(slug=identifier))


def set_aliases(obj, aliases):
    if type(aliases) == str:
        obj.aliases.clear()
        for alias_text in aliases.split(','):
            alias_text = alias_text.strip()
            if not alias_text:
                continue
            alias, _ = TitleAlias.objects.get_or_create(alias=alias_text)
            obj.aliases.add(alias)


def update_specs(table: SpecificationTable, data: List[Dict]):
    spec_ids = {spec['id'] for spec in data if spec.get('id')}
    spec_id_prev = {spec.id for spec in table.specification_set.all()}
    deletables = spec_id_prev - spec_ids
    delete_db_objects(Specification, deletables)
    for spec_data in data:
        spec_id = spec_data.get('id')
        spec_title= spec_data.get('title')
        if spec_id:
            spec = Specification.objects.get(pk=spec_id, table=table)
            if spec.title != spec_title:
                spec.title = spec_title
                spec.save()
        else:
            spec = Specification.objects.create(table=table, title=spec_title)
        set_aliases(spec, spec_data['aliases'])


def update_cat_tables(cat: Category, data: List[Dict]):
    table_ids_prev = {t.id for t in cat.specificationtable_set.all()}
    table_ids_now = {table['id'] for table in data if table.get('id')}
    deltables = table_ids_prev - table_ids_now
    delete_db_objects(SpecificationTable, deltables)
    for table_data in data:
        table_id = table_data.get('id')
        table_title= table_data.get('title')
        if table_id:
            table = SpecificationTable.objects.get(pk=table_id, category=cat)
            if table.title != table_title:
                table.title = table_title
                table.save()
        else:
            table = SpecificationTable.objects.create(category=cat, title=table_title)
        if aliases:=table_data.get('aliases'):
            set_aliases(table, aliases)
        update_specs(table, table_data['specs'])


def update_product_specs(product: Product, tables):
    for table_data in tables:
        for spec_data in table_data['specs']:
            if value:=spec_data['value']:
                table_spec = Specification.objects.get(id=spec_data['id'], table__id=table_data['id'])
                prod_spec = ProductSpec.objects.filter(specification=table_spec, product=product).first()
                if prod_spec:
                    prod_spec.value = value
                    prod_spec.save()
                else:
                    ProductSpec.objects.create(
                        product = product,
                        specification = table_spec,
                        value = value
                    )
            else:
                prod_spec = ProductSpec.objects.filter(specification__id=spec_data['id'], product=product).first()
                if prod_spec:
                    prod_spec.delete()


def manage_product_prev_images(product, existing_images):
    prev_image_ids = [pimg.id for pimg in product.productimage_set.all()]
    existing_image_ids = [eimg['id'] for eimg in existing_images]
    deletable_ids = list(set(prev_image_ids) - set(existing_image_ids))
    deletables = ProductImage.objects.filter(id__in=deletable_ids)
    if deletables.count():
        deletables.delete()


def manage_product_prev_keyfeatures(product, keyfeatures_data):
    kf_data_with_id = filter(lambda kf: kf.get('id'), keyfeatures_data)
    prev_kf_ids = [kf.id for kf in product.keyfeature_set.all()]
    existing_kf_ids = [kf['id'] for kf in kf_data_with_id]
    deletable_ids = list(set(prev_kf_ids) - set(existing_kf_ids))
    deletables = KeyFeature.objects.filter(id__in=deletable_ids)
    if deletables.count():
        deletables.delete()
    


def filter_products(slug: str, request):
    pricefrom = request.GET.get('pricefrom')
    priceto = request.GET.get('priceto')
    tags = request.GET.get('tags')
    availibility = request.GET.get('availibility')
    if tags:
        tag_id_list = list(map(int, tags.split(',')))
        products_with_tag_count = Product.objects.annotate(
            matching_tags_count=Count('tags', filter=Q(tags__id__in=tag_id_list))
        )
        filtered_products = products_with_tag_count.filter(
            Q(matching_tags_count=len(tag_id_list)) &
            (Q(category__slug=slug) | Q(tags__slug=slug))
        ).distinct()
    else:
        filtered_products = Product.objects.filter(Q(category__slug=slug) | Q(tags__slug=slug)).distinct()
    if pricefrom and priceto:
        pricefrom = int(pricefrom)
        priceto = int(priceto)
        filtered_products = filtered_products.filter(price__gte=pricefrom, price__lte=priceto)
    if availibility:
        availibility_list = list(map(lambda s: bool(int(s)), availibility.split(',')))
        filtered_products = filtered_products.filter(in_stock__in=availibility_list)
    return filtered_products


def get_cart(request) -> Cart:
    new_cart_args = {}
    if request.user.is_authenticated:
        cart = Cart.objects.filter(owner=request.user, checked_out=False).first()
        if cart:
            return cart
        else:
            new_cart_args['owner'] = request.user
    elif cartid:=request.data.get('cartid'):
        cart = Cart.objects.filter(cartid=cartid).first()
        if cart:
            return cart
    cart = Cart.objects.create(**new_cart_args)
    return cart


def update_wlist_products(wlist: WishList, prod_ids):
    products = Product.objects.filter(id__in=prod_ids)
    removable = list(set(wlist.products.all()) - set(products))
    wlist.products.add(*products)
    wlist.products.remove(*removable)


def perform_wishlist_initiation(request) -> WishList:
    new_wishlist_args = {}
    wl_id = request.GET.get('id')
    wishlist_obj = WishList.objects.filter(id=wl_id).first()
    if request.user.is_authenticated:
        wlist_temp = WishList.objects.filter(owner=request.user).first()
        if wlist_temp:
            wishlist_obj = wlist_temp
        elif wishlist_obj and wishlist_obj.owner is None:
            wishlist_obj.owner = request.user
            wishlist_obj.save()
        else:
            new_wishlist_args['owner'] = request.user
    if wishlist_obj is None:
        wishlist_obj = WishList.objects.create(**new_wishlist_args)
    return wishlist_obj


def perform_wishlist_sync(request) -> WishList:
    product_ids = request.data.get('products')
    print('syncing prods: {}'.format(product_ids), flush=1)
    wishlist_obj = get_object_or_404(WishList, id=request.data.get('id'))
    update_wlist_products(wishlist_obj, product_ids)
    return wishlist_obj


def update_cart(cart: Cart, cartinfo: dict):
    prod_ids = list(map(int, cartinfo.keys()))
    cart_products = [cart_prod for cart_prod in cart.cartproduct_set.all()]
    for cart_prod in cart_products:
        if cart_prod.product.id not in prod_ids:
            cart_prod.delete()
    for pid in cartinfo.keys():
        product = get_object_or_404(Product, pk=pid)
        cart_prod, _ = CartProduct.objects.get_or_create(cart=cart, product=product)
        cart_prod.quantity = cartinfo[pid]
        cart_prod.save()


def get_coupon_discount_amount(cart: Cart, coupon: Coupon):
    if coupon.expiry < timezone.now():
        raise ValidationError('Expired Coupon')
    items_count, cart_total_amount = cart.cart_total()
    if cart_total_amount < coupon.min_spend:
        raise ValidationError(f'You have to spend at least {coupon.min_spend} to apply this coupon')
    return coupon.get_discount_amount(cart_total_amount)


# def get_payable_amount(cartid, couponcode):

def update_cart_checked_out(cart: Cart, request):
    if request.user.is_authenticated:
        cart.owner = request.user
    else:
        cart.owner = None
    cart.checked_out = True
    cart.save()


def get_shipping_charges(item_count, location):
    charge_per_item = settings.SHIPPING_CHARGES.get(location)
    if not charge_per_item:
        charge_per_item = settings.SHIPPING_CHARGES['outside']
    return charge_per_item * item_count


def change_order_status(order: Order):
    if order.status in ['delivered', 'cancelled']:
        raise ValidationError('Cannot Change Status Now')
    newstatus_idx = settings.ORDER_STATUS_FLOW.index(order.status) + 1
    newstatus = settings.ORDER_STATUS_FLOW[newstatus_idx]
    order.status = newstatus
    OrderStatusTimestamp.objects.create(
        order = order,
        status = newstatus
    )
    order.save()
    

def cancel_order(order: Order):
    if order.status in ['delivered', 'cancelled']:
        raise ValidationError('Cannot cancel order now')
    newstatus = "cancelled"
    order.status = newstatus
    OrderStatusTimestamp.objects.create(
        order = order,
        status = newstatus
    )
    order.save()
    

def perform_undo_status_change(order: Order):
    offset_time = timezone.now() - settings.STATUS_UNDO_TIMEOUT
    current_status_ts = order.orderstatustimestamp_set.filter(
        status = order.status,
        completed_at__gte = offset_time
    ).first()
    if not current_status_ts:
        raise ValidationError('Cannot undo status change')
    newstatus = settings.ORDER_STATUS_FLOW[0]
    if order.status == 'cancelled':
        last_timestamp = OrderStatusTimestamp.objects.filter(
            order = order
        ).exclude(
            id = current_status_ts.id
        ).order_by(
            '-completed_at'
        ).first()
        if last_timestamp:
            newstatus = last_timestamp.status
    else:
        curr_status_idx = settings.ORDER_STATUS_FLOW.index(order.status)
        if curr_status_idx > 0:
            newstatus = settings.ORDER_STATUS_FLOW[curr_status_idx-1]
    current_status_ts.delete()
    order.status = newstatus
    order.save()
    