from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    
    def add_goods_to_the_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        login_link.click()
        
    def is_name_of_goods_and_price_equal(self):
        assert self.name_of_goods_in_basket() == self.name_of_goods_at_product_page(), "Name of goods at product page not equal name in the basket"
        assert self.price_of_goods_at_product_page() == self.price_of_goods_in_basket(), "Price of goods at product page not equal price in the basket"
        
        
    def price_of_goods_at_product_page(self):
        price_at_product_page = self.browser.find_element(*ProductPageLocators.PRICE_OF_GOODS).text
        return price_at_product_page

    def price_of_goods_in_basket(self):
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_OF_GOODS_IN_BASKET).text
        return price_in_basket

    def name_of_goods_at_product_page(self):
        name_of_goods = self.browser.find_element(*ProductPageLocators.NAME_OF_GOODS).text
        return name_of_goods
    
    def name_of_goods_in_basket(self):
        name_of_goods_in_basket = self.browser.find_element(*ProductPageLocators.NAME_OF_GOODS_IN_BASKET).text
        return name_of_goods_in_basket 
    
    
    