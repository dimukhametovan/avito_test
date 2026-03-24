import allure
from src.pages.main_page import MainPage
from src.assertions.main_page_assertions import MainAssertions


@allure.title('2. Сортировка "По цене"')
def test_desktop_sort_by_price(desktop_driver, base_url):
    page = MainPage(desktop_driver, base_url)

    with allure.step("Открыть главную страницу"):
        page.open_main()
        page.wait_for_loaded()

    with allure.step('Выбрать сортировку "По цене"'):
        page.select_sort_by_price()

    with allure.step("Проверить, что цены отсортированы по убыванию"):
        prices = page.get_ad_prices()
        MainAssertions.ads_sorted_by_price_desc(prices)
