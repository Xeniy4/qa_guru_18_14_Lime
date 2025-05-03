
import allure

from pages.shop_pages import Authorization

auth = Authorization()



@allure.epic("Web UI тесты")
@allure.story('Проверка авторизации с невалидным номером телефона')
def test_auth_no_valid_mobile():
    with allure.step('Открыть главную страницу'):
        auth.open()

    with allure.step('Нажать на кнопку "Личный кабинет"'):
        auth.open_lk()

    with allure.step('Нажать на кнопку "Войти или зарегистрироваться"'):
        auth.click_button_enter()

    with allure.step('Ввести невалидный номер телефона'):
        auth.type_mobile('58458456215')

    with allure.step('Нажать на кнопку "Получить код"'):
        auth.click_button_det_code()

    with allure.step('Проверка текста ошибки: "Некорректный номер телефона"'):
        auth.check_error_text_mobile('Некорректный номер телефона')



