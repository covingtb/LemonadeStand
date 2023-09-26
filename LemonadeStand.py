# Author: Brenden Covington
# GitHub username: covingtb
# Date: 7/3/2023
# Description: Program that creates object classes for tracking menu items, sales, and operations of a lemonade
# stand (or stands) that are added


class MenuItem:
    """Creates object class of menu items that have a name, cost, and selling price"""
    def __init__(self, name, wholesale_cost, selling_price):
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        """Returns name of menu item"""
        return self._name

    def get_wholesale_cost(self):
        """Returns cost of menu item"""
        return self._wholesale_cost

    def get_selling_price(self):
        """Returns selling price of menu item"""
        return self._selling_price


class SalesForDay:
    """Creates object class of sales for each day with the number of day and a dictionary of sales"""

    def __init__(self, day, sales_dict):
        self._day = day
        self._sales_dict = sales_dict

    def get_day(self):
        """Returns the day"""
        return self._day

    def get_sales_dict(self):
        """Returns the sales dictionary"""
        return self._sales_dict


class LemonadeStand:
    """Creates class object for lemonade stands that utilizes the last two classes and multiple
    methods to record the business"""

    def __init__(self, name):
        self._name = name
        self._day = 0
        self._menu = {}
        self._sales_record = []

    def get_name(self):
        """Returns name of stand"""
        return self._name

    def add_menu_item(self, menu_item):
        """Adds menu item to private menu"""
        self._menu[menu_item.get_name()] = menu_item

    def enter_sales_for_today(self, sales_dict):
        """Adds sales for day for each menu item in the sales dictionary, and none if the item doesn't exist"""
        try:
            for sale in sales_dict:
                if sale not in self._menu:
                    raise InvalidSalesItemError("Item not in menu")
            sales_for_day = SalesForDay(self._day, sales_dict)
            self._sales_record.append(sales_for_day)
            self._day += 1
        except InvalidSalesItemError as e:
            print(e)

    def sales_of_menu_item_for_day(self, day, menu_item):
        """Returns the sales of a certain menu item on a specific day"""
        if day < 0 or day >= len(self._sales_record):
            return 0
        sales_day = self._sales_record[day]
        sales_dict = sales_day.get_sales_dict()
        return sales_dict.get(menu_item, 0)

    def total_sales_for_menu_item(self, item_name):
        """Returns total sales for input menu item since opening"""
        total_sales = 0
        for sale in self._sales_record:
            sales_dict = sale.get_sales_dict()
            if item_name in sales_dict:
                total_sales += sales_dict[item_name]
        return total_sales

    def total_profit_for_menu_item(self, item_name):
        """Returns total profit for input menu item since opening"""
        total_sales = self.total_sales_for_menu_item(item_name)
        item = self._menu[item_name]
        total_profit = total_sales * (item.get_selling_price() - item.get_wholesale_cost())
        return total_profit

    def total_profit_for_stand(self):
        """Returns total profit for all items in the stand added together since opening"""
        total_profit = 0
        for item in self._menu:
            total_profit += self.total_profit_for_menu_item(item)
        return total_profit


class InvalidSalesItemError(Exception):
    """Adds InvalidSalesItemError error message as an object for use in the enter_sales_for_today to
    avoid program collapse"""
    pass


if __name__ == "__main__":
    stand = LemonadeStand('Lemons R Us')
    item1 = MenuItem('lemonade', .5, 1.5)
    stand.add_menu_item(item1)
    item2 = MenuItem('cookie', .2, 1)
    stand.add_menu_item(item2)
    day0 = {
        'lemonade': 5,
        'cookie': 2
    }
    try:
        stand.enter_sales_for_today({'cupcake': 1})
    except InvalidSalesItemError as e:
        print(e)
    stand.enter_sales_for_today(day0)
    print(f"lemonade profit = {stand.total_profit_for_menu_item('lemonade')}")
