import json

import pytest
import requests
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from task_3.models import Product

pytestmark = pytest.mark.django_db


def header():
    url = 'http://service/api/v1/task_1/token/'
    body = {
        "username": "admin",
        "password": "1"
    }

    response = requests.post(url, data=body)
    token = json.loads(response.text)
    headers = {
        'Authorization': f"Bearer {token['access']}",
        'Content-Type': 'application/json'
    }
    return headers


get_header = header()


def test_retrieve_product():
    client = APIClient()
    product = Product.objects.create(name='Product 1', price='10.00', description='Description 1')
    retrieve_url = reverse('product-detail', args=[product.id])
    response = client.get(retrieve_url, headers=get_header)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == 'Product 1'


def test_create_product():
    client = APIClient()
    url = reverse('product-list')
    data = {
        'name': 'New Product',
        'price': '15.00',
        'description': 'New Description',
        'status': 'start'
    }
    response = client.post(url, data, headers=get_header)
    assert response.status_code == status.HTTP_201_CREATED
    assert Product.objects.last().name == 'New Product'


def test_update_product():
    client = APIClient()
    product = Product.objects.create(name='Product 1', price='10.00', description='Description 1')
    update_url = reverse('product-detail', args=[product.id])
    data = {
        'name': 'Updated Product',
        'price': '25.00',
        'description': 'Updated Description',
        'status': 'finish'
    }
    response = client.patch(update_url, data, headers=get_header)
    assert response.status_code == status.HTTP_200_OK
    assert Product.objects.get(id=product.id).name == 'Updated Product'


def test_list_products():
    client = APIClient()
    url = reverse('product-list')
    response = client.get(url, headers=get_header)
    assert response.status_code == status.HTTP_200_OK


def test_delete_product():
    client = APIClient()
