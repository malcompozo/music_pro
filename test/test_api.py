from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
import json
import os

from services.models import Products, Category
from core.api.serializers import ProductsSerializer, CategorySerializer




class CategoryAPITest(APITestCase):

    def setUp(self):
        self.category_url = reverse('categoria')


    def test_create_category_from_file(self):
        file_path = os.path.join(os.path.dirname(__file__), 'MOCK_DATA.json')
        with open(file_path) as file:
            data_list = json.load(file)

        for data in data_list:
            response = self.client.post(self.category_url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(Category.objects.count(), len(data_list))

    def test_create_category(self):
        data = {
            'id': 1,
            'categoria': [],
            'nom_category': 'Test Category',
            'description': 'Test Description'
        }

        response = self.client.post(self.category_url, data, format='json')
        
        self.assertEqual(Category.objects.get().nom_category, 'Test Category')
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

    def test_get_category(self):
        category = Category.objects.create(
            id = '1',
            nom_category = 'Test Get Category',
            description = 'Test Description'
        )

        product = Products.objects.create(
            id='1',
            nom_product='Guitarra',
            subtitle='jibson',
            descripcion='electrica',
            image='https://pixabay.com/es/photos/guitarra-guitarra-el%C3%A9ctrica-2925274/',
            value=250000,
            category=category
        )

        url = reverse('categoria_id', args=[category.pk])
        response = self.client.get(url)

        serializer = CategorySerializer(instance=category)
        expected_data = serializer.data

        self.assertEqual(response.data, expected_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK) 


    def test_update_category(self):
        category = Category.objects.create(
            id = '1',
            nom_category = 'Test Get Category',
            description = 'Test Description'
        )

        product = Products.objects.create(
            id='1',
            nom_product='Guitarra',
            subtitle='jibson',
            descripcion='electrica',
            image='https://pixabay.com/es/photos/guitarra-guitarra-el%C3%A9ctrica-2925274/',
            value=250000,
            category=category
        )

        url = reverse('categoria_id', args=[category.pk])
        data = {
            'id': 1,
            'nom_category': 'Updated Category',
            'description': 'Updated Description'
        }

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category.refresh_from_db()
        self.assertEqual(category.nom_category, 'Updated Category')

    def test_delete_category(self):
        category = Category.objects.create(
            id = '1',
            nom_category = 'Test Get Category',
            description = 'Test Description'
        )

        product = Products.objects.create(
            id='1',
            nom_product='Guitarra',
            subtitle='jibson',
            descripcion='electrica',
            image='https://pixabay.com/es/photos/guitarra-guitarra-el%C3%A9ctrica-2925274/',
            value=250000,
            category=category
        )

        url = reverse('categoria_id', args=[category.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0) 



########################### Products TESTS ###########################
class ProductsAPITest(APITestCase):

    def setUp(self):
        self.product_url = reverse('productos')
        self.category_url = reverse('categoria')

    def test_create_product(self):
        category = Category.objects.create(
            id = '1',
            nom_category='Test Category',
            description='Test Description'
        )

        data = {
            'id': 1,
            'nom_product': 'Test Product',
            'subtitle': 'Test Subtitle',
            'descripcion': 'Test Description',
            'image': 'test_image.jpg',
            'value': 10,
            'category': category.id
        }

        response = self.client.post(self.product_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Products.objects.count(), 1)
        self.assertEqual(Products.objects.get().nom_product, 'Test Product') 

    def test_get_product(self):
        category = Category.objects.create(
            id='1',
            nom_category='Test Get Category',
            description='Test Description'
        )

        product = Products.objects.create(
            id=1,
            nom_product='Guitarra',
            subtitle='jibson',
            descripcion='electrica',
            image='https://pixabay.com/es/photos/guitarra-guitarra-el%C3%A9ctrica-2925274/',
            value=250000,
            category=category
        )

        url = reverse('productos_id', args=[product.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = ProductsSerializer(instance=product)
        expected_data = serializer.data
        expected_data['category'] = str(category.pk)
        response.data['category'] = str(response.data['category'])
        self.assertEqual(response.data, expected_data)


    def test_update_product(self):
        category1 = Category.objects.create(
            id=1,
            nom_category='Category 1',
            description='Category 1 Description'
        )

        category2 = Category.objects.create(
            id=2,
            nom_category='Category 2',
            description='Category 2 Description'
        )

        product = Products.objects.create(
            id=1,
            nom_product='Test Product',
            subtitle='Test Subtitle',
            descripcion='Test Description',
            image='test_image.jpg',
            value=10,
            category=category1
        )

        url = reverse('productos_id', args=[product.pk])
        data = {
            'id': 1,
            'nom_product': 'Updated Product',
            'subtitle': 'Updated Subtitle',
            'descripcion': 'Updated Description',
            'image': 'updated_image.jpg',
            'value': 20,
            'category': category2.id
        } 

        response = self.client.put(url, data, format='json')


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product.refresh_from_db()
        self.assertEqual(product.nom_product, 'Updated Product')

    def test_delete_product(self):
        category = Category.objects.create(
            id = '1',
            nom_category = 'Test Get Category',
            description = 'Test Description'
        )

        product = Products.objects.create(
            id=1,
            nom_product='Test Product',
            subtitle='Test Subtitle',
            descripcion='Test Description',
            image='test_image.jpg',
            value=10,
            category=category
        )
        url = reverse('productos_id', args=[product.pk])
        response = self.client.delete(url)

        #import pdb
        #pdb.set_trace()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Products.objects.count(), 0)


