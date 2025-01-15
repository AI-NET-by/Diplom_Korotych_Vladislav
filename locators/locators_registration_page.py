import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("REGISTRATION_URL") or 'https://ru.pinterest.com/ideas'

        super().__init__(web_driver, url)

    btn_login = WebElement(xpath='//div[@data-test-id ="simple-login-button"]')
    btn_sign_up = WebElement(xpath='//div[@data-test-id ="simple-signup-button"]')
    btn_registration = WebElement(xpath='//div[@data-test-id="emailSignUpButton"]')
    btn_enter_google = WebElement(xpath='//div[@data-test-id="google-connect-button"]')
    btn_terms_of_service = WebElement(xpath='//div[@data-test-id="tos"]')
    btn_privacy = WebElement(xpath='//div[@data-test-id="privacy"')
    btn_notice = WebElement(xpath='//div[@data-test-id="noticeAtCollection"]')
    btn_your_Enter = WebElement(xpath='//div[@data-test-id="login-signup-toggle"]')

    img_page_ideas = ManyWebElements(xpath='//div[@data-test-id="interestRep"]')
    img_page_search = ManyWebElements(xpath='//div[@data-test-id="search-suggestion-today-bubble"]')
    btn_search = WebElement(xpath='(//div[@data-test-id="search-box-container"])[1]')

