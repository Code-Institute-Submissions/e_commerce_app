from django.test import TestCase
from .models import Product, Category


class TestServiceViews(TestCase):
    def test_get_products_page(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_service_details_page(self):
        categories = Category(name="Category Name")
        categories.save()
        product_detail = Product(name="Test product", price=999.00,
                                 description="Test product description",
                                 image="test.jpg")
        product_detail.save()

        response = self.client.get("/products/1/")
        self.assertEqual(response.status_code, 200)
