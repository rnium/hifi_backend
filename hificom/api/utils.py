from typing import Dict, List
from hificom.models import (Category, SpecificationTable, 
                            Specification, ProductSpec, ProductImage, 
                            TitleAlias, Product, Cart, CartProduct, Coupon)
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
                prod_spec = ProductSpec.objects.filter(specification__id=spec_data['id']).first()
                if prod_spec:
                    prod_spec.delete()


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
    discount_amount = 0
    print(cart_total_amount, flush=1)
    if percent:=coupon.discount_percent:
        discount_draft = (cart_total_amount * percent) / 100
        if max_dis:=coupon.max_amount:
            discount_amount = min(max_dis, discount_draft)
        else:
            discount_amount = discount_draft
    elif discount:=coupon.discount_amount:
        discount_amount = min(cart_total_amount, discount)
    return discount_amount


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