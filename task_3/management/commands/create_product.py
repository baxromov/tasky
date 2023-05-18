import random

from django.core.management.base import BaseCommand
from faker import Faker

from task_3 import models


class Command(BaseCommand):
    help = "Create products with random data"

    def add_arguments(self, parser):
        parser.add_argument('num_products', type=int, help='Number of products to create')

    def handle(self, *args, **options):
        num_products = options['num_products']
        fake = Faker()
        for _ in range(num_products):
            name = fake.name()
            price = random.uniform(1, 1000)
            description = fake.text()

            product = models.Product.objects.create(
                name=name,
                price=price,
                description=description
            )
            print(f"Created product: {product}")
