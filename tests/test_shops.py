from pages.for_tests import Authorization,SelectShop, ShoppingCart
import allure

auth = Authorization()
select_shop = SelectShop()
shopping_card = ShoppingCart()


def test_select_specific_shop():
    with allure.step('Открыть главную страницу'):
        auth.open()

    with allure.step('Нажать на кнопку Личный кабинет'):
        auth.open_lk()

    with allure.step('Нажать на кнопку Магазины'):
        select_shop.click_shops()

    with allure.step('Нажать на выпадающий список магазинов'):
        select_shop.click_dropdown()

    with allure.step('Нажать на город'):
        select_shop.select_city('Благовещенск')

    with allure.step('Выбрать гендер Женщины'):
        select_shop.select_gender()

    with allure.step('Проверка отображения магазина'):
        select_shop.check_shop_name('"ТРЦ «ОСТРОВА»"')


def test_open_product_card():
    with allure.step('Открыть главную страницу'):
        auth.open()

    with allure.step('Нажать на Бургер меню'):
        shopping_card.open_burger_menu()

    with allure.step('Нажать на Новинки'):
        shopping_card.click_novelties()

    with allure.step('Нажать на Фильтр'):
        shopping_card.open_filter()

    with allure.step('Нажать на цвет'):
        shopping_card.select_color('оливковый')

    with allure.step('Закрыть фильтр'):
        shopping_card.close_filter()

    with allure.step('Нажать на товар'):
        shopping_card.select_product()

    with allure.step('Нажать на добавить в корзину'):
        shopping_card.click_add_cart()

    with allure.step('Проверка текста на кнопке'):
        shopping_card.check_text_size('Выберите размер')


