import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: cs, da, de, en-bg, el, es, fi, \
                                            fr, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-hans.\
                                            Default is ru")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart chrome browser for test..")
    options = Options()
    language_of_browser = request.config.getoption("language")
    options.add_experimental_option('prefs', {'intl.accept_languages': language_of_browser})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()



