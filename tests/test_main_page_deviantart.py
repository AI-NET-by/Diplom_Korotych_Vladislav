import time

import allure
import pytest_check as check

from locators.locators_main_page_deviantart import MainPage
from conftest import web_browser



@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки хедара')
def test_headers(web_browser):
    """Этот тест проверяет хедер главной страницы"""

    page = MainPage(web_browser)

    elements_headers = [(page.btn_blog, "Блог", "https://ru.pinterest.com/_/_/blog/?utm_source=organicpins_pinsite_homepageicon&utm_campaign=pinterest_homepage_blogicon_all_evergreen&utm_medium=organic-pinterest"),
                        (page.btn_sign_up, "Регистрация","https://ru.pinterest.com/#top"),
                        (page.btn_description, "Описание", "https://ru.pinterest.com/_/_/about/"),
                        (page.btn_login, "Регистрация", "https://ru.pinterest.com/#top"),
                        (page.btn_business, "Бизнес", "https://ru.pinterest.com/_/_/business/"),
                        (page.btn_ideas, "Просмотреть","https://ru.pinterest.com/ideas/"),
                        (page.btn_android,"Приложение для Android", "https://play.google.com/store/apps/details?id=com.pinterest"),
                        (page.btn_iphone,"Приложение для iPhone", "https://play.google.com/store/apps/details?id=com.pinterest"),
                        (page.btn_privacy,"Пользователи", "https://www.pinterest.com/html_sitemap/pinners_a.html"),
                        (page.btn_today,"Сегодня", "https://ru.pinterest.com/today/"),
                        (page.btn_collections,"Коллекции", "https://www.pinterest.com/html_sitemap/boards_a.html")]

    for elements, text_element, url_elements in elements_headers:
        with allure.step('Тест проверки правильного URL при переходе'):
             elements.click()
             page.switch_to_window()

        with allure.step('Тест проверки отображения на экране'):
             check.is_true(elements.is_visible())

        with allure.step('Тест проверки кликабельности'):
             check.is_true(elements.is_clickable())

    # with allure.step('Тест проверки орфографии'):
    #     page.btn_blog.click()
    #     page.switch_to_window(1)
    #     print(page.get_current_url())

@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки хедара')
def test_search_box_container(web_browser):
    """"Этот тест проверяет кликабельность, наличие элементов, правописание"""

    page = MainPage(web_browser)

    with allure.step('Проверка, что в поиске есть вкладка dolled Up home decor'):
        check.is_true(page.search_box_container.is_visible())

    with allure.step('Нажимаем на вкладку dolled Up home decor'):
        page.dolled_up_home_decor.click()

    with allure.step('Проверяем, что мы перешли по вкладке'):
        check.equal(page.get_current_url(), 'https://ru.pinterest.com/today/best/dolled-up-home-decor/123788/')


