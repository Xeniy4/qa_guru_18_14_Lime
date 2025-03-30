from pages.for_tests import Authorization, Search
import allure

auth = Authorization()
search = Search()

def test_search_product():
    with allure.step('Открыть главную страницу'):
        auth.open()

    with allure.step('Нажать на кнопку поиск'):
        search.click_button_search()

    with allure.step('Написать в поиске значение'):
        search.type_search_text('Футболка')

    with allure.step('Нажать на товар'):
        search.select_product()

    with allure.step('Проверка отображения текста товара'):
        search.check_text('Футболка поло oversize в полоску')
