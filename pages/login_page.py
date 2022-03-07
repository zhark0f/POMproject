from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string


class LoginPage(BasePage):

    @staticmethod
    def create_a_new_user():
        letters_and_digits = [_ for _ in string.ascii_letters]
        letters_and_digits.extend([str(i) for i in range(0, 10)])
        letters_and_digits.extend(["_", "-"])
        random.shuffle(letters_and_digits)
        len_of_email = random.randint(1, 20)
        user_email = random.sample(letters_and_digits, len_of_email)
        user_email.append("@gmail.com")
        len_of_password = random.randint(9, 15)
        user_password = random.sample(letters_and_digits, len_of_password)
        return "".join(user_email), "".join(user_password)

    def register_new_user(self, email, password):
        self.browser.find_element(
            *LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD_1).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD_2).send_keys(password)
        WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable(LoginPageLocators.REGISTRATION_BUTTON)).click()
        

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, f"expected 'login' to be substring of '{self.browser.current_url}'"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Register form is not presented"
