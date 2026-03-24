import time
import allure
from src.pages.main_page import MainPage
from src.pages.stats_page import StatsPage
from src.assertions.stats_page_assertions import StatsAssertions


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
        StatsAssertions.auto_update_is_running(is_running)

    with allure.step('Отключить автообновление (кнопка "Пауза")'):
        stats.click_toggle()
        time_running_before = stats.get_timer_value()
        time.sleep(2.0)
        time_still = stats.get_timer_value()

        StatsAssertions.timer_stopped(time_running_before, time_still)

    with allure.step('Включить автообновление (кнопка "Продолжить")'):
        stats.click_toggle()
        is_running = stats.is_auto_update_running()
        StatsAssertions.auto_update_is_running(is_running)