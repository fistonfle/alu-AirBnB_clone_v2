#!/usr/bin/python3
"""Unit tests for Review class"""

import unittest
from models.place import Place
from models.user import User
from tests.test_models.test_base_model import TestBaseModel
from models.review import Review


class TestReview(TestBaseModel):
    """Test Review class"""

    def __init__(self, *args, **kwargs):
        """Initialize TestReview instance"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id_attribute(self):
        """Test setting the place_id attribute of Review"""
        new_review = self.value()
        place = Place()
        new_review.place_id = place.id
        self.assertEqual(type(new_review.place_id), str)

    def test_user_id_attribute(self):
        """Test setting the user_id attribute of Review"""
        new_review = self.value()
        user = User()
        new_review.user_id = user.id
        self.assertEqual(type(new_review.user_id), str)

    def test_text_attribute(self):
        """Test setting the text attribute of Review"""
        new_review = self.value()
        new_review.text = ""
        self.assertEqual(type(new_review.text), str)


if __name__ == '__main__':
    unittest.main()
