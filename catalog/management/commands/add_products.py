from itertools import product

from django.core.management.base import BaseCommand
from unicodedata import category
from django.db import connection
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add products to the database'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1;")
            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1;")

        category_1, _ = Category.objects.get_or_create(name='Продуткы', description='Продукты питания')
        category_2, _ = Category.objects.get_or_create(name='Одежда', description='Повседневная одежда')

        products_1 = [
            {'name': 'Помидоры', 'description': 'Помидоры минусинские', 'price': 330, 'category': category_1},
            {'name': 'Яблоки', 'description': 'Яблоки голден', 'price': 260, 'category': category_1},
        ]

        products_2 = [
            {'name': 'Джинсы', 'description': 'Джинсовая одежда', 'price': 3030, 'category': category_2},
            {'name': 'Кофты', 'description': 'Вязанные кофты', 'price': 2600, 'category': category_2},
        ]

        for product_data in products_1:
            products, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {products.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exist: {products.name}'))

        for product_data in products_2:
            products, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {products.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exist: {products.name}'))