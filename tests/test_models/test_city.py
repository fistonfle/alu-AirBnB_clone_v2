#!/usr/bin/python3
"""Unit tests for City class"""

import unittest
from models.state import State
from tests.test_models.test_base_model import TestBaseModel
from models.city import City

class TestCity(TestBaseModel):
    """Test City class"""

    def __init__(self, *args, **kwargs):
        """Initialize TestCity instance"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id_attribute(self):
        """Test setting the state_id attribute of City"""
        state = State()
        new_city = self.value()
        new_city.state_id = state.id
        self.assertEqual(type(new_city.state_id), str)

    def test_name_attribute(self):
        """Test setting the name attribute of City"""
        new_city = self.value()
        new_city.name = "Batch"
        self.assertEqual(type(new_city.name), str)


if __name__ == '__main__':
    unittest.main()
