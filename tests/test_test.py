import allure
from selene import browser

@allure.story('тесты для фейла')
def test_passed():
    with allure.step('Открываем главную страницу'):
        browser.config.window_width = 1900
        browser.config.window_height = 1080
        browser.open("https://githubcom")

