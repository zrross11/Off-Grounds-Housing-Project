import unittest
from django.test import TestCase
from ..models import HousingOption
from django.urls import reverse


class ViewsTests(TestCase):
    # def setUp(self):
        # HousingOption.objects.create(name="house01", address="1", numberOfBedrooms=1)
        # HousingOption.objects.create(name="house2")

    def test_login_view(self):
        response = self.client.get(reverse('housing:housing_listing'))
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
