from pages.shop_pages import Authorization,SelectShop, ShoppingCart
import allure

auth = Authorization()
select_shop = SelectShop()
shopping_card = ShoppingCart()


@allure.story('Проверка поиска конкретного магазина на странице "Магазины"')
def test_select_specific_shop():
    with allure.step('Открыть главную страницу'):
        auth.open()

    with allure.step('Нажать на кнопку "Личный кабинет"'):
        auth.open_lk()

    with allure.step('Нажать на кнопку "Магазины"'):
        select_shop.click_shops()

    with allure.step('Нажать на выпадающий список магазинов'):
        select_shop.click_dropdown()

    with allure.step('Нажать на город'):
        select_shop.select_city('Благовещенск')

    with allure.step('Проверка отображения магазина'):
        select_shop.check_shop_name('ТРЦ «ОСТРОВА»')


@allure.story('Проверка функционала поиска и добавления товара в "Избранное" через фильтр')
def test_add_favorites():
    with allure.step('Открыть главную страницу'):
        auth.open()

    with allure.step('Нажать на "Бургер меню"'):
        shopping_card.open_burger_menu()

    with allure.step('Нажать на "Новинки"'):
        shopping_card.click_novelties()

    with allure.step('Нажать на "Фильтр"'):
        shopping_card.open_filter()

    with allure.step('Нажать на цвет'):
        shopping_card.select_color('черный')

    with allure.step('Закрыть фильтр'):
        shopping_card.close_filter()

    with allure.step('Нажать на товар'):
        shopping_card.select_product()

    with allure.step('Нажать на кнопку "Добавить в Избранное"'):
        shopping_card.click_add_favourites()

    with allure.step('Нажать на "Избранное"'):
        shopping_card.click_favorites()

    with allure.step('Проверить отображение добавленного товара'):
        shopping_card.check_text_favorites('ЮБКА')


