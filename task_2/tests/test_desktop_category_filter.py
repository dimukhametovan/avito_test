import allure
from src.pages.main_page import MainPage
from src.assertions.main_page_assertions import MainAssertions


@allure.title('3. Фильтр "Категория"')
def test_desktop_category_filter(desktop_driver, base_url):
    page = MainPage(desktop_driver, base_url)

    with allure.step("Открыть главную страницу"):
        page.open_main()
        page.wait_for_loaded()

    with allure.step("Выбрать первую категорию"):
        page.select_first_category()

    with allure.step("Проверить, что все объявления одной категории"):
        categories = page.get_ad_categories()
        MainAssertions.all_ads_have_same_category(categories)
