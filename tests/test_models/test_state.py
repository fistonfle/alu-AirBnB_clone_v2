#!/usr/bin/python3
"""Unit tests for State class"""

import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.state import State


class TestState(TestBaseModel):
    """Test State class"""

    def test_name_property(self):
        """Test the 'name' property of State"""
        new_state = State()
        new_state.name = "Arizona"
        self.assertEqual(type(new_state.name), str)


if __name__ == '__main__':
    unittest.main()
