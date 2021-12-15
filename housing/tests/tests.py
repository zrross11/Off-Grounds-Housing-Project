import unittest
from django.test import TestCase
from ..models import HousingOption


class HousingTestCase(unittest.TestCase):
    def test_housing_name(self):
        HousingOption.objects.create(name="house01", address="1", numberOfBedrooms=1)
        house_one = HousingOption.objects.get(name="house01")
        self.assertEqual(house_one.name, "house01")

    def test_housing_price_default(self):
        HousingOption.objects.create(name="house02")
        house_two = HousingOption.objects.get(name="house02")
        self.assertEqual(house_two.pricePerUnit, 0)

if __name__ == '__main__':
    unittest.main()
