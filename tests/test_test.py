import allure
from selene import browser

@allure.story('тесты для фейла')
def test_passed():
    assert False

