from .base_page import BasePage
from selenium.webdriver.common.by import By


class StatsPage(BasePage):
    stats_title = 'h1._title_mv9k4_23'

    refresh_button = 'button._refreshButton_ir5wu_16'
    toggle_button = 'button._toggleButton_ir5wu_69'
    time_value = 'span._timeValue_ir5wu_112'
    auto_update_label = 'span._timeLabel_ir5wu_106'
    progress_fill = 'div._progressFill_ir5wu_129'

    def wait_for_open(self, timeout: int = 10):
        self.wait_for_element(self.stats_title, timeout)

    def wait_for_timer(self, timeout: int = 10):
        self.wait_for_element(self.time_value, timeout)

    def click_refresh(self):
        self.click(self.refresh_button)

    def click_toggle(self):
        self.click(self.toggle_button)

    def get_timer_value(self, timeout: int = 10) -> str:
        self.wait_for_timer(timeout)
        return self.get_text(self.time_value)

    def get_progress_width(self, timeout: int = 10) -> float:
        self.wait_for_timer(timeout)
        style = self.get_attribute(self.progress_fill, "style")
        try:
            part = style.split("width:")[1].split("%")[0]
            return float(part.strip())
        except Exception:
            return 0.0

    def is_auto_update_running(self) -> bool:
        btn = self.driver.find_element(By.CSS_SELECTOR, self.toggle_button)
        label = btn.get_attribute("aria-label") or ""
        return "Отключить автообновление" in label
