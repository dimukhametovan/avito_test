import allure
from src.pages.main_page import MainPage
from src.assertions.main_page_assertions import MainAssertions


@allure.title('1. Фильтр "Диапазон цен"')
def test_desktop_price_filter(desktop_driver, base_url):
    page = MainPage(desktop_driver, base_url)
    min_value = 10000
    max_value = 15000

    with allure.step("Открыть главную страницу"):
        page.open_main()
        page.wait_for_loaded()

    with allure.step("Прокрутить до фильтра и проверить его отображение"):
        page.scroll_to_price_filter()
        MainAssertions.price_filter_visible_with_correct_title(page)
        MainAssertions.price_filter_has_two_inputs(page)

    with allure.step("Задать диапазон цен"):
        page.set_price_range(min_value, max_value)

    with allure.step("Проверить, что все объявления в заданном диапазоне"):
        prices = page.get_ad_prices()
        MainAssertions.ads_prices_within_range(prices, min_value, max_value)
