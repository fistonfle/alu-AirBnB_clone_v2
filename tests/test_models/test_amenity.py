#!/usr/bin/python3
"""Unit tests for Amenity class"""

import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


class TestAmenity(TestBaseModel):
    """Test Amenity class"""

    def __init__(self, *args, **kwargs):
        """Initialize Amenity test instance"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name(self):
        """Test the 'name' attribute of Amenity"""
        new_amenity = self.value()
        new_amenity.name = "amenity"
        self.assertEqual(type(new_amenity.name), str)


if __name__ == '__main__':
    unittest.main()
