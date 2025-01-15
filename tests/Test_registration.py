import time

import allure
import pytest_check as check
from locators.locators_reg_page import RegistrationPage
from conftest import web_browser


@allure.story('Тест для проверки страницы регистрации')
@allure.feature('Тест для проверки работоспособности инпута')
def test_input_main_registration(web_browser):
    """Этот тест проверяет работоспособность инпута"""

    page = RegistrationPage(web_browser)

    page.btn_sign_up.click()
    page.btn_eye.click()
    page.password_field_input.send_keys("1234567890")
    page.birthdate_field.send_keys("01122000")
    page.email_field_input.send_keys("test@gmail.com")
    time.sleep(2)
    page.btn_registration_confirm.click()
    time.sleep(2)
    with allure.step("Тест проверки на заполняемое поле"):
        check.is_not_none(page.password_field_input)
        check.is_not_none(page.email_field_input)
        check.is_not_none(page.birthdate_field)
    with allure.step("Тест проверки на выпадающее окно при введении неверных данных"):
        check.is_true(page.protect_window_text.is_visible())

