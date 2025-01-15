
import requests
import allure
import pytest
import pytest_check as check

@allure.story('Тест проверки статус кода на "название своего сайта"')
@allure.feature('Тест для проверки статус кода на главной странице')

def test_API_MainPage():
    """ Этот тест проверяет статус код главной страницы сайта """

    url = "https://ru.pinterest.com/"

    payload = {}
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'cm_sub=denied; _b="AX/52+ZgwZtDGJDrfdC9oXpy++xOprFLsDWT1+rgP6r7WJtZgqpO+3v7GnnEh7qHZwg="; _derived_epik=dj0yJnU9SktlSVl3VmhTQjg0VUkwanZEbXVXQ2NBQzhIOU9vcnombj1iU0swXzdKM2FjWHZVaW9kOXhmWF93Jm09MSZ0PUFBQUFBR2JrTllVJnJtPTEmcnQ9QUFBQUFHYmtOWVUmc3A9Mg; ar_debug=1; csrftoken=c06b01aacbaf25c496ce5d73727dd5bf; _routing_id="d2653cb3-b33a-4168-b521-4162cb4b9fc6"; sessionFunnelEventLogged=1; _auth=0; l_o=b284aElLakpXdExGazJyVGw2b0d0NWJIZ3FHUmZHR3YzY0dDczY5d2pPcW4wSHNIREFyYnJ1d0czZkVGTGM1eWN3WTQrZS9jTHBYMXR1M2FtcWYzV3FSWlIyVEk0MEFDS3BWblByNzkwRFk9Jml0amdFRUd6OThKanRmNFBWWU9tWlNqVGh4MD0=; __Secure-s_a=NXh4S1ZsTjlUcllpcTdwSklRbUdaVGZPSTNnckI3UjdqenFYaGhITHFxND0mOWwrSmVvdnI4U29IQkNjdjEyYVNaZm51SjNRPQ==; fba=True; _pinterest_sess=TWc9PSZUVzBsY1YxMG5CU2dEZys0ODM1cnE0MG1jMDJSZmliZ0JMalpqUjlRTmtZWWhuN20xVFJVczEzb3FrRVV5SUYrdjE3TldRem1sU0dMRGZORXJ4QmdMYjlpYkZFUnc5elF1YysxcjN0Qjlrcz0meUZpY1ppdi9OL2YvVVVxNi94cTlWWCtlNE40PQ==',
    'priority': 'u=0, i',
    'referer': 'https://www.yandex.by/clck/jsredir?from=yandex.by;suggest;browser&text=',
    'sec-ch-ua': '"Not?A_Brand";v="99", "Chromium";v="130"',
    'sec-ch-ua-full-version-list': '"Not?A_Brand";v="99.0.0.0", "Chromium";v="130.0.6723.152"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.status_code)

    with allure.step("Проверка статуса кода на главной странице"):
        check.equal(response.status_code, 200, f'Статус код не равен 200. Статус код равен {response.status_code}')