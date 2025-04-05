import pytest

from pages.shop_pages import Authorization
import allure

auth = Authorization()

@pytest.fixture
def auth_page():
    yield Authorization()

@allure.story('Проверка авторизации с невалидным номером телефона')
def test_auth_no_valid_mobile(auth_page):
    with allure.step('Открыть главную страницу'):
        auth_page.open()

    with allure.step('Нажать на кнопку Личный кабинет'):
        auth_page.open_lk()

    with allure.step('Нажать на кнопку Войти или зарегистрироваться'):
        auth_page.click_button_enter()

    with allure.step('Ввести невалидный номер телефона'):
        auth_page.type_mobile('58458456215')

    with allure.step('Нажать на кнопку Получить код'):
        auth_page.click_button_det_code()

    with allure.step('Проверка текста ошибки: "Некорректный номер телефона"'):
        auth_page.check_error_text_mobile('Некорректный номер телефона')



