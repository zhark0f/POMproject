from .pages.product_page import ProductPage
import pytest

# pytest -v -s --language=ru test_product_page.py


list_of_promo_numbers = [0, 1, 2, 3, 4, 5, 6,
                        pytest.param(7, marks=pytest.mark.xfail), 8, 9]


@pytest.mark.parametrize('promo_number', list_of_promo_numbers)
def test_guest_can_add_product_to_basket(browser, promo_numbers):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207?promo=offer{promo_numbers}"
    page = ProductPage(browser, link)
    page.open()
    page.add_goods_to_the_basket()
    page.solve_quiz_and_get_code()
    page.is_name_of_goods_and_price_equal()
