import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage


class MainPage(BasePage):
    price_filter_section = 'aside._sidebar_tw7kk_74 div._filters__group_1iunh_1:nth-of-type(4)'
    price_filter_title = (
        'aside._sidebar_tw7kk_74 div._filters__group_1iunh_1:nth-of-type(4) '
        '> label._filters__label_1iunh_8'
    )    
    price_min_input = (
        'aside._sidebar_tw7kk_74 div._filters__group_1iunh_1:nth-of-type(4) '
        'div._filters__priceRange_1iunh_118 input._filters__input_1iunh_20[placeholder="От"]'
    )
    price_max_input = (
        'aside._sidebar_tw7kk_74 div._filters__group_1iunh_1:nth-of-type(4) '
        'div._filters__priceRange_1iunh_118 input._filters__input_1iunh_20[placeholder="До"]'
    )

    ads_list = 'div._cards_imlvm_176 > div._card_15fhn_2'
    ad_price = 'div._card__price_15fhn_241'
    ad_category = 'div._card__category_15fhn_259'

    sort_select = 'div._filtersBar__sort_1lsyo_71 div._filters__group_1iunh_1:nth-of-type(1) select._filters__select_1iunh_21'

    category_select = 'aside._sidebar_tw7kk_74 div._filters__group_1iunh_1:nth-of-type(2) select._filters__select_1iunh_21'

    urgent_toggle = 'label._urgentToggle_h1vv9_1'

    urgent_label = 'label._urgentToggle_h1vv9_1 span._urgentToggle__slider_h1vv9_21'

    priority_filter = 'aside._sidebar_tw7kk_74 div._filters__group_1iunh_1:nth-of-type(3) select._filters__select_1iunh_21'

    theme_button = 'button._themeToggle_127us_1'

    stats_nav_link = 'nav._nav_14hw7_1 a._link_14hw7_51[href="/stats"]'

    def open_main(self):
        self.open("/")

    def scroll_to_price_filter(self):
        self.scroll_into_view(self.price_filter_section)

    def set_price_range(self, min_value: int, max_value: int):
        self.type(self.price_min_input, str(min_value))
        self.type(self.price_max_input, str(max_value))
        time.sleep(1) 

    def select_sort_by_price(self):
        select_el = self.driver.find_element(By.CSS_SELECTOR, self.sort_select)
        Select(select_el).select_by_value("price")
        time.sleep(1)

    def select_first_category(self):
        select_el = self.driver.find_element(By.CSS_SELECTOR, self.category_select)
        options = select_el.find_elements(By.TAG_NAME, "option")
        if len(options) > 1:
            options[1].click()
        time.sleep(1)  

    def toggle_urgent(self):
        self.click(self.urgent_toggle)
        time.sleep(1)

    def go_to_stats(self):
        self.click(self.stats_nav_link)

    def toggle_theme(self):
        self.click(self.theme_button)

    def get_ad_prices(self):
        ads = self.find_all(self.ads_list)
        prices = []
        for ad in ads:
            el = ad.find_element(By.CSS_SELECTOR, self.ad_price)
            text = el.text
            normalized = "".join(ch for ch in text if ch.isdigit())
            if normalized:
                prices.append(int(normalized))
            time.sleep(0.1)
        return prices

    def get_ad_categories(self):
        ads = self.find_all(self.ads_list)
        categories = []
        for ad in ads:
            el = ad.find_element(By.CSS_SELECTOR, self.ad_category)
            categories.append(el.text)
        return categories

    def get_urgent_flags(self):
        ads = self.find_all(self.ads_list)
        flags = []
        for ad in ads:
            els = ad.find_elements(By.CSS_SELECTOR, self.urgent_label)
            flags.append(len(els) > 0)
        return flags

    def get_priority_filter_value(self) -> str:
        return self.get_text(self.priority_filter)

    def get_theme_button_text(self) -> str:
        return self.get_text(self.theme_button)
    
    def wait_for_loaded(self, timeout: int = 10):
        self.wait_for_element(self.ads_list, timeout)
    
    def get_html_theme(self) -> str:
        html = self.driver.find_element(By.TAG_NAME, "html")
        return html.get_attribute("data-theme")
