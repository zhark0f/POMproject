from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LANGUAGE_OF_PAGE = (By.CSS_SELECTOR, "option[selected='selected']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group > [class='btn btn-default']")
    BASKET_GOODS = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_TEXT_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    BESKET_TEXT_CONTINUE_SHOPPING =(By.CSS_SELECTOR, "#content_inner > p > a")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#id_registration-redirect_url + button.btn-primary")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_OF_GOODS = (By.CSS_SELECTOR, ".product_main > p.price_color")
    NAME_OF_GOODS = (By.CSS_SELECTOR, ".product_main > h1")
    PRICE_OF_GOODS_IN_BASKET = (By.CSS_SELECTOR, ".alertinner > p > strong")
    NAME_OF_GOODS_IN_BASKET = (By.CSS_SELECTOR, ".alertinner > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
