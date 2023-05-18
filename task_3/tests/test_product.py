from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from task_3.models import Product


class ProductAPITest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.product1 = Product.objects.create(name='Product 1', price='10.00', description='Description 1')
        self.product2 = Product.objects.create(name='Product 2', price='20.00', description='Description 2')
        self.url = reverse('product-list')

    def authenticate_client(self):
        self.client.login(username='testuser', password='testpass')

    def test_list_products(self):
        self.authenticate_client()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_product(self):
        retrieve_url = reverse('product-detail', args=[self.product1.id])
        self.authenticate_client()
        response = self.client.get(retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product1.name)

    def test_create_product(self):
        data = {
            'name': 'New Product',
            'price': '15.00',
            'description': 'New Description',
            'status': 'start'
        }
        self.authenticate_client()
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 3)
        self.assertEqual(Product.objects.last().name, 'New Product')

    def test_update_product(self):
        update_url = reverse('product-detail', args=[self.product1.id])
        data = {
            'name': 'Updated Product',
            'price': '25.00',
            'description': 'Updated Description',
            'status': 'finish'
        }
        self.authenticate_client()
        response = self.client.patch(update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.get(id=self.product1.id).name, 'Updated Product')

    def test_delete_product(self):
        delete_url = reverse('product-detail', args=[self.product1.id])
        self.authenticate_client()
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 1)
