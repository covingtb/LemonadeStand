# Author: Brenden Covington
# GitHub username: covingtb
# Date: 7/3/2023
# Description: Program that tests object classes for tracking menu items, sales, and operations of a lemonade
# stand (or stands) that are added to the program LemonadeStand.py
import unittest
from LemonadeStand import *


class TestLemonadeStand(unittest.TestCase):
    """Adds test case class for different methods in the Lemonade Stand file"""
    def setUp(self):
        """Sets up menu items for test"""
        self.stand = LemonadeStand('Lemons R Us')
        self.item1 = MenuItem('lemonade', .5, 1.5)
        self.stand.add_menu_item(self.item1)
        self.item2 = MenuItem('cookie', .2, 1)
        self.stand.add_menu_item(self.item2)
        self.day0 = {
            'lemonade': 5,
            'cookie': 2
        }

    def test_init(self):
        """Tests the test case for expected outputs"""
        self.assertEqual(self.stand.get_name(), 'Lemons R Us')
        self.assertEqual(self.stand._day, 0)
        self.assertEqual(self.stand._menu, {'lemonade': self.item1, 'cookie': self.item2})
        self.assertEqual(self.stand._sales_record, [])

    def test_add_menu_item(self):
        """Tests to see if the menu is set up correctly and adding items, like chocolate, correctly"""
        self.assertEqual(self.stand._menu, {'lemonade': self.item1, 'cookie': self.item2})
        item3 = MenuItem('chocolate', .3, 1.5)
        self.stand.add_menu_item(item3)
        self.assertEqual(self.stand._menu, {'lemonade': self.item1, 'cookie': self.item2, 'chocolate': item3})

    def test_enter_sales_for_today(self):
        """Tests enter sales for today method"""
        self.assertRaises(InvalidSalesItemError, self.stand.enter_sales_for_today, {'cupcake': 1})
        self.stand.enter_sales_for_today(self.day0)
        self.assertEqual(self.stand._day, 1)
        self.assertEqual(len(self.stand._sales_record), 1)

    def test_sales_of_menu_item_for_day(self):
        """Tests expected outputs for different sales numbers on different days"""
        self.stand.enter_sales_for_today(self.sales_dict)

        day = 0
        item_name = "lemonade"
        self.assertEqual(self.stand.sales_of_menu_item_for_day(day, item_name), 20)

        day = 0
        item_name = "cookie"
        self.assertEqual(self.stand.sales_of_menu_item_for_day(day, item_name), 10)

        day = 1
        item_name = "lemonade"
        self.assertEqual(self.stand.sales_of_menu_item_for_day(day, item_name), 0)

    def test_total_sales_for_menu_item(self):
        """Tests sales for specific item on day 0 through tested date"""
        self.stand.enter_sales_for_today(self.day0)
        self.assertEqual(self.stand.total_sales_for_menu_item('lemonade'), 5)

    def test_total_profit_for_menu_item(self):
        """Tests total profit for menu item from day 0 to 2.5"""
        self.stand.enter_sales_for_today(self.day0)
        self.assertEqual(self.stand.total_profit_for_menu_item('lemonade'), 2.5)

    def test_total_profit_for_stand(self):
        """Tests total profit for stand from day 0 to 3.5"""
        self.stand.enter_sales_for_today(self.day0)
        self.assertEqual(self.stand.total_profit_for_stand(), 3.5)


if __name__ == '__main__':
    unittest.main()
