# Навигация

- [Что реализовано](#что-реализовано)
- [Как запустить тесты](#как-запустить-тесты)
- [Allure reports скриншоты](#allure-reports-скриншоты)
- [Отчет о локальном запуске тестов](#отчет-о-локальном-запуске-тестов)

## Что реализовано

1. Используется паттерн Page Object для автотестов
2. Классы страниц, проверок и тестов хранятся отдельно
3. Есть интеграция с allure, тесты размечены шагами
4. Tech stack: python, selenium, allure

## Как запустить тесты

```bash
# создать и активировать виртуальное окружение
python -m venv .venv
source .venv/bin/activate

# перейти в папку проекта
cd ./task_2

# установить зависимости
pip install -r requirements.txt

# запустить тесты и открыть allure report
pytest tests --alluredir=allure-results
allure serve allure-results
```

## Allure-reports скриншоты

![test_1](./allure%20report/test_1.png)
![test_2](./allure%20report/test_2.png)
![test_3](./allure%20report/test_3.png)
![test_4](./allure%20report/test_4.png)
![test_5](./allure%20report/test_5.png)
![test_6](./allure%20report/test_6.png)

## Отчет о локальном запуске тестов

```bash
================================================ test session starts =================================================
platform win32 -- Python 3.13.3, pytest-9.0.2, pluggy-1.6.0
rootdir: D:\озон тестовое\ozon_test\task_2
configfile: pytest.ini
plugins: allure-pytest-2.15.3
collected 6 items

tests\test_desktop_category_filter.py .                                                                         [ 16%]
tests\test_desktop_price_filter.py F                                                                            [ 33%]
tests\test_desktop_sort_by_price.py .                                                                           [ 50%]
tests\test_desktop_stats_timer.py F                                                                             [ 66%]
tests\test_desktop_urgent_toggle.py F                                                                           [ 83%]
tests\test_mobile_theme.py .                                                                                    [100%]

====================================================== FAILURES ======================================================
_____________________________________________ test_desktop_price_filter ______________________________________________

desktop_driver = <selenium.webdriver.chrome.webdriver.WebDriver (session="437ff775116c077651b032bc27f60337")>
base_url = 'https://cerulean-praline-8e5aa6.netlify.app'

    @allure.title('Фильтр "Диапазон цен"')
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
>           MainAssertions.ads_prices_within_range(prices, min_value, max_value)

tests\test_desktop_price_filter.py:26:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

prices = [16683, 15060, 17092, 17764, 15068, 15753, ...], min_value = 10000, max_value = 15000

    @staticmethod
    def ads_prices_within_range(prices, min_value: int, max_value: int):
        assert prices, "Список цен пуст"
        for price in prices:
>           assert min_value <= price <= max_value, f"Цена {price} не в диапазоне {min_value}-{max_value}"
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E           AssertionError: Цена 16683 не в диапазоне 10000-15000

src\assertions\main_page_assertions.py:20: AssertionError
______________________________________________ test_desktop_stats_timer ______________________________________________

desktop_driver = <selenium.webdriver.chrome.webdriver.WebDriver (session="9e05ce6b85232398f523d626302b921d")>
base_url = 'https://cerulean-praline-8e5aa6.netlify.app'

    @allure.title("5. Управление таймером обновления статистики")
    def test_desktop_stats_timer(desktop_driver, base_url):
        main = MainPage(desktop_driver, base_url)
        stats = StatsPage(desktop_driver, base_url)

        with allure.step("Открыть главную страницу"):
            main.open_main()
            main.wait_for_loaded()

        with allure.step('Перейти в раздел "Статистика"'):
            main.go_to_stats()
            stats.wait_for_open()
            stats.wait_for_timer()

        with allure.step('Нажать "Обновить" и проверить перезапуск таймера'):
            before_time = stats.get_timer_value()
            before_progress = stats.get_progress_width()

            stats.click_refresh()
            time.sleep(1.0)

            after_time = stats.get_timer_value()
            after_progress = stats.get_progress_width()

            StatsAssertions.timer_restarted(before_time, after_time)
            StatsAssertions.progress_after_refresh(before_progress, after_progress)

        with allure.step("Проверить, что автообновление сейчас включено"):
            is_running = stats.is_auto_update_running()
>           StatsAssertions.auto_update_is_running(is_running)

tests\test_desktop_stats_timer.py:37:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

is_running = True

    @staticmethod
    def auto_update_is_running(is_running: bool):
>       assert not is_running, "Автообновление должно быть выключено"
               ^^^^^^^^^^^^^^
E       AssertionError: Автообновление должно быть выключено

src\assertions\stats_page_assertions.py:18: AssertionError
_____________________________________________ test_desktop_urgent_toggle _____________________________________________

desktop_driver = <selenium.webdriver.chrome.webdriver.WebDriver (session="c57821e806bb34087c9604aa597cf464")>
base_url = 'https://cerulean-praline-8e5aa6.netlify.app'

    @allure.feature('Десктоп — тоггл "Только срочные"')
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
>           MainAssertions.all_ads_urgent(flags)

tests\test_desktop_urgent_toggle.py:20:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

flags = [False, False, False, False, False, False, ...]

    @staticmethod
    def all_ads_urgent(flags):
        assert flags, "Список объявлений пуст"
>       assert all(flags), "Не все объявления имеют метку 'Срочно'"
               ^^^^^^^^^^
E       AssertionError: Не все объявления имеют метку 'Срочно'

src\assertions\main_page_assertions.py:37: AssertionError
============================================== short test summary info ===============================================
FAILED tests/test_desktop_price_filter.py::test_desktop_price_filter - AssertionError: Цена 16683 не в диапазоне 10000-15000
FAILED tests/test_desktop_stats_timer.py::test_desktop_stats_timer - AssertionError: Автообновление должно быть выключено
FAILED tests/test_desktop_urgent_toggle.py::test_desktop_urgent_toggle - AssertionError: Не все объявления имеют метку 'Срочно'
============================================ 3 failed, 3 passed in 55.92s ============================================

```
