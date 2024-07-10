from typing import Dict, List
from hificom.models import Category, SpecificationTable, Specification, ProductSpec, ProductImage, TitleAlias, Product
from django.db.models import Model


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
                prod_spec = ProductSpec.objects.filter(specification=table_spec).first()
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

def add_product_images(product: Product, images):
    img_list = [{'product': product, 'main': img} for img in images]
