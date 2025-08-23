from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED

def get_products_from_cache():
    """Получение списка продуктов из кэша, либо запись из БД в кэш"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'products_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_products_by_category_from_cache(category_id):
    """Получение списка продуктов по категории из кэша, либо запись из БД в кэш"""
    if not CACHE_ENABLED:
        return Product.objects.filter(category_id=category_id)

    key = f'products_category_{category_id}'
    products = cache.get(key)
    if products is not None:
        return products

    products = Product.objects.filter(category_id=category_id)
    cache.set(key, products)
    return products
