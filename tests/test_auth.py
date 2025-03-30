
from pages.for_tests import Authorization
import allure

auth = Authorization()
#работает
def test_auth(browser_manager):
    with allure.step('Открыть главную страницу'):
        auth.open()

    with allure.step('Нажать на кнопку Личный кабинет'):
        auth.open_lk()

    with allure.step('Нажать на кнопку Войти или зарегистрироваться'):
        auth.click_button_enter()

    with allure.step('Ввести невалидный номер телефона'):
        auth.type_mobile('58458456215')

    with allure.step('Нажать на кнопку Получить код'):
        auth.click_button_det_code()

    with allure.step('Проверка текста ошибки: "Некорректный номер телефона"'):
        auth.check_error_text_mobile('Некорректный номер телефона')



