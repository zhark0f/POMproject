from .base_page import BasePage
from .locators import BasketLocators
from .locators import BasePageLocators


class BasketPage(BasePage):
    
    def should_not_be_goods_in_basket(self):
        assert self.is_not_element_present(*BasketLocators.BASKET_GOODS), \
            "Goods in basket, but should not be"
    
    def text_in_basket_should_be_basket_empty(self):
        language_of_page = self.browser.find_element(*BasePageLocators.LANGUAGE_OF_PAGE).get_attribute("value")
        temp_message_of_basket = self.browser.find_element(*BasketLocators.BASKET_TEXT_BASKET_EMPTY).text
        delete_part_of_message = self.browser.find_element(*BasketLocators.BESKET_TEXT_CONTINUE_SHOPPING).text
        message_of_basket_empty = temp_message_of_basket.replace(delete_part_of_message, "").strip()
        assert languages[language_of_page] == message_of_basket_empty, "message in basket isn\'t 'basket empty'"
        
        
languages = {
    "ar": "سلة التسوق فارغة",
    "ca": "La seva cistella està buida.",
    "cs": "Váš košík je prázdný.",
    "da": "Din indkøbskurv er tom.",
    "de": "Ihr Warenkorb ist leer.",
    "en": "Your basket is empty.",
    "el": "Το καλάθι σας είναι άδειο.",
    "es": "Tu carrito esta vacío.",
    "fi": "Korisi on tyhjä",
    "fr": "Votre panier est vide.",
    "it": "Il tuo carrello è vuoto.",
    "ko": "장바구니가 비었습니다.",
    "nl": "Je winkelmand is leeg",
    "pl": "Twój koszyk jest pusty.",
    "pt": "O carrinho está vazio.",
    "pt-br": "Sua cesta está vazia.",
    "ro": "Cosul tau este gol.",
    "ru": "Ваша корзина пуста",
    "sk": "Váš košík je prázdny",
    "uk": "Ваш кошик пустий.",
    "zh-cn": "Your basket is empty.",
}