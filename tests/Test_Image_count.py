import time

import allure
import pytest_check as check
from locators.locators_registration_page import MainPage

from conftest import web_browser


@allure.story('Тест для проверки количества картинок')
@allure.feature('Тест для проверки совпадения количества картинок')
def test_Pafe_ideas(web_browser):
    '''Этот тест проверяет количество картинок, которое равно 13'''

    page = MainPage(web_browser)

    check.equal(13, page.img_page_ideas.count())

def test_search_ideas(web_browser):
    '''Этот тест проверяет количество картинок, которое равно 4'''

    page = MainPage(web_browser)
    page.btn_search.click()
    check.equal(page.img_page_search.count(), 4)