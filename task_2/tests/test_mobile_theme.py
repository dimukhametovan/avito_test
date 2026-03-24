import allure
from src.assertions.main_page_assertions import MainAssertions
from src.pages.main_page import MainPage

@allure.title("6. Переключение между темной и светлой темами")
def test_mobile_theme_toggle(mobile_driver, base_url):
    page = MainPage(mobile_driver, base_url)

    with allure.step("Открыть главную страницу"):
        page.open_main()
        page.wait_for_loaded()
        before_theme = page.get_html_theme()

    with allure.step("Нажать на кнопку изменения темы"):
        page.toggle_theme()

    with allure.step("Проверить, что тема изменилась"):
        after_theme = page.get_html_theme()
        MainAssertions.theme_changed(after_theme, before_theme)
