from pages.shop_pages import Authorization, Subscribe
import allure

auth = Authorization()
subscribe = Subscribe()


@allure.epic("Web UI тесты")
@allure.story('Проверка подписки в футере')
def test_subscribe_footer():
    with allure.step('Открыть страницу "Избранное"'):
        auth.open_favorites()

    with allure.step('Принять куки'):
        subscribe.accept_cookie()

    with allure.step('В футере нажать на кнопку "Подписаться"'):
        subscribe.click_button_subscribe()

    with allure.step('Написать валидную почту'):
        subscribe.type_email('test123@test.com')

    with allure.step('Включить чекбокс "Женщины"'):
        subscribe.checkbox()

    with allure.step('Нажать на кнопку "Подписаться"'):
        subscribe.click_button_subscribe_page_subscribe()

    with allure.step('Проверка текста ошибки'):
        subscribe.check_error_subscribe('Необходимо подтвердить согласие')
