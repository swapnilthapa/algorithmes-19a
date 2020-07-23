import unittest
from testing.new import Operations
from classes.Item import *


class MyTest(unittest.TestCase):
    item = Item()

    def test_add(self):
        abc = Operations()
        actual_result = abc.add(5, 6)
        expected_result = 11
        self.assertEqual(expected_result, actual_result)

    def test_check_even_no(self):
        op = Operations()
        actual_result = op.check_even_no(6)
        # expected_result = True
        # self.assertEqual(expected_result, actual_result)
        self.assertTrue(actual_result)

    def test_check_even_no(self):
        op = Operations()
        actual_result = op.check_even_no(5)
        self.assertFalse(actual_result)

    def test_add_item(self):
        result = self.item.add_item('test_item', 'test_type', 100)
        self.assertTrue(result)

    def test_add_item_view(self):
        result = self.item.add_item('', '', 100)
        self.assertFalse(result)

    def test_add_item_view(self):
        result = self.item.add_item('test', 'type', 'asd')
        self.assertFalse(result)

    def test_add_item_view(self):
        result = self.item.add_item('', '', -100)
        self.assertFalse(result)

    def test_show_items(self):
        data = self.item.show_item()
        actual_result = len(data)
        expected_result = 9
        self.assertEqual(expected_result, actual_result)

    def test_search_item(self):
        data = self.item.search_item('momo')
        actual_result = len(data)
        expected_result = 2
        self.assertEqual(expected_result, actual_result)

    def test_search_items1(self):
        data = self.item.search_item('noodle')
        actual_result = len(data)
        expected_result = 0
        self.assertEqual(expected_result, actual_result)




