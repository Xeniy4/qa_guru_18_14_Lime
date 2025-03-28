from selene import browser, have

BUTTON_LK = '[arial-label="account-link"]'
GENDER_WOMAN = '"Женщины"'
BURGER_MENU = '.toolbar__main__logo .burger'

#Написано
class Authorization:
    def open(self):
        browser.open('/')

    def open_lk(self):
        browser.element(BUTTON_LK).click()

    def click_button_enter(self):
        browser.element('.btn-primary').click()

    def type_mobile(self,value):
        browser.element('#tel').type(value)

    def click_button_det_code(self):
        browser.element('.FormGroupSubmit .btn-block').click()

    def check_error_text_mobile(self,value):
        browser.element('.FormGroup__helper').should(have.text(value))

#Написано
class SelectShop:
    def open_lk(self):
        browser.element(BUTTON_LK).click()

    def click_shops(self):
        browser.element('.AccountMenu__Item [href="/ru_ru/about"]').click()

    def click_dropdown(self):
        browser.element('.DropdownList__header').click()

    def select_city(self, value):
        browser.element(f'//div/span[contains(text(),"{value}")]').click()

    def select_gender(self):
        browser.element(f'//label/span[contains(text(),"{GENDER_WOMAN}")]').click()

    def check_shop_name(self,value):
        browser.element('.text--uppercase').should(have.text(value))


class Subscribe:
    def click_button_subscribe(self):
        browser.element('.ModernFooter-subscribe__btn').click()

    def type_email(self,value):
        browser.element('#ssb_footer').type(value)

    def checkbox(self):
        browser.element(f'.form-subscribe__container .checkbox__element[value="{GENDER_WOMAN}"]')

    def click_button_subscribe(self):
        browser.element('.form-subscribe__container .btn-block').click()

    def check_error_subscribe(self,value):
        browser.element('.FormGroup__helper').should(have.text(value))

#Написано
class ShoppingCart:
    def open_burger_menu(self):
        browser.element(BURGER_MENU).click()

    def click_novelties(self):
        browser.element('[href="/ru_ru/catalog/new"]').click()

    def open_filter(self):
        browser.element('.filter-button__title').click()

    def select_color(self,value):
        browser.element(f'//label/span[contains(text(),"{value}")]').click()

    def close_filter(self):
        browser.element('.IButtonClose').click()

    def select_product(self):
        browser.element('.CatalogProduct__title').click()

    def click_add_cart(self):
        browser.element('.btn-cart').click()

    def check_text_size(self,value):
        browser.element('.btn-cart._outline').should(have.text(value))

#Написано
class Search:
    def click_button_search(self):
        browser.element('.toolbar__main .SearchBox__button').click()

    def type_search_text(self,value):
        browser.element('.toolbar__main .SearchBox__input').type(value).press_enter()

    def select_product(self):
        browser.element('.CatalogProduct__title [href="/ru_ru/product/23770_3594_753-sinii_zelenyi"]')

    def check_text(self,value):
        browser.element(f'//div/h1[contains(text(),"{value}")]').should(have.text(value))




 #   browser.element()


