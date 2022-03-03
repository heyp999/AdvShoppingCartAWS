import unittest
import adshopcart_methods as methods
from time import sleep
import adshopcart_locators as locators


# unittest case
class ShoppingCartAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_advantage_shopping_cart_case2():
        methods.setup()
        methods.check_homepage()
        methods.register_new_user()
        methods.logout()
        methods.login(locators.new_username, locators.new_password)
        methods.del_current_user()
        methods.check_user_account_deleted(locators.new_username, locators.new_password)
        methods.teardown()


if __name__ == '__main__':
    unittest.main()
