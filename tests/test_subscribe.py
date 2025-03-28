from pages.for_tests import Authorization, Subscribe
import allure

auth = Authorization()
subscribe = Subscribe()

def test_subscribe_footer():
    with allure.step('Открыть главную страницу'):
        auth.open()

    with allure.step('В футере нажать на кнопку Подписаться'):
        subscribe.click_button_subscribe()

    with allure.step('Написать валижную почту'):
        subscribe.type_email('test123@test.com')

    with allure.step('Включить чекбокс Женщины'):
        subscribe.checkbox()

    with allure.step('Нажать на кнопку Подписаться'):
        subscribe.click_button_subscribe()

    with allure.step('Проверка текста ошибки'):
        subscribe.check_error_subscribe('Необходимо подтвердить согласие')
