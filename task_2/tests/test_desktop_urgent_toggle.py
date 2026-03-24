import allure
from src.pages.main_page import MainPage
from src.assertions.main_page_assertions import MainAssertions


@allure.title('4. Тоггл "Только срочные"')
def test_desktop_urgent_toggle(desktop_driver, base_url):
    page = MainPage(desktop_driver, base_url)

    with allure.step("Открыть главную страницу"):
        page.open_main()
        page.wait_for_loaded()

    with allure.step('Включить тоггл "Только срочные"'):
        page.toggle_urgent()

    with allure.step('Проверить метку "Срочно" у всех объявлений'):
        flags = page.get_urgent_flags()
        MainAssertions.all_ads_urgent(flags)

    with allure.step('Проверить, что фильтр "Приоритет" = "Срочный"'):
        value = page.get_priority_filter_value()
        MainAssertions.priority_filter_is_urgent(value)
