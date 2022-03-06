from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_OF_GOODS = (By.CSS_SELECTOR, ".product_main > p.price_color")
    NAME_OF_GOODS = (By.CSS_SELECTOR, ".product_main > h1")
    PRICE_OF_GOODS_IN_BASKET = (By.CSS_SELECTOR, ".alertinner > p > strong")
    NAME_OF_GOODS_IN_BASKET = (By.CSS_SELECTOR, ".alertinner > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
