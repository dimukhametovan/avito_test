from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver, base_url: str):
        self.driver = driver
        self.base_url = base_url.rstrip("/")

    def open(self, path: str = "/"):
        self.driver.get(f"{self.base_url}{path}")

    def click(self, selector: str):
        element = self.driver.find_element(By.CSS_SELECTOR, selector)
        element.click()

    def type(self, selector: str, value: str):
        element = self.driver.find_element(By.CSS_SELECTOR, selector)
        element.clear()
        element.send_keys(value)

    def get_text(self, selector: str) -> str:
        element = self.driver.find_element(By.CSS_SELECTOR, selector)
        return element.text

    def is_displayed(self, selector: str) -> bool:
        element = self.driver.find_element(By.CSS_SELECTOR, selector)
        return element.is_displayed()

    def find_all(self, selector: str):
        return self.driver.find_elements(By.CSS_SELECTOR, selector)

    def scroll_into_view(self, selector: str):
        element = self.driver.find_element(By.CSS_SELECTOR, selector)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def get_attribute(self, selector: str, name: str) -> str:
        element = self.driver.find_element(By.CSS_SELECTOR, selector)
        return element.get_attribute(name)

    def wait_for_element(self, selector: str, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
        )
