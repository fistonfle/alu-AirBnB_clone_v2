#!/usr/bin/python3
"""Unit tests for User class"""

# flake8: noqa

import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.user import User

class TestUser(TestBaseModel):
    """Test User class"""

    def __init__(self, *args, **kwargs):
        """Initialize TestUser instance"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name_attribute(self):
        """Test setting the first_name attribute of User"""
        new_user = self.value()
        new_user.first_name = "Chyna"
        self.assertEqual(type(new_user.first_name), str)

    def test_last_name_attribute(self):
        """Test setting the last_name attribute of User"""
        new_user = self.value()
        new_user.last_name = "Chyna"
        self.assertEqual(type(new_user.last_name), str)

    def test_email_attribute(self):
        """Test setting the email attribute of User"""
        new_user = self.value()
        new_user.email = "angoyewally@gmail.com"
        self.assertEqual(type(new_user.email), str)

    def test_password_attribute(self):
        """Test setting the password attribute of User"""
        new_user = self.value()
        new_user.password = "123aashja"
        self.assertEqual(type(new_user.password), str)


if __name__ == '__main__':
    unittest.main()
