import pytest
from src.pages.main_page import MainPage


class MainAssertions:
  @staticmethod
  def price_filter_visible_with_correct_title(page: MainPage):
      assert page.is_displayed(page.price_filter_section), "Секция фильтра по цене не отображается"
      assert page.get_text(page.price_filter_title) == "Диапазон цен (₽)", "Неверный заголовок фильтра по цене"

  @staticmethod
  def price_filter_has_two_inputs(page: MainPage):
      assert page.is_displayed(page.price_min_input), "Поле минимальной цены не отображается"
      assert page.is_displayed(page.price_max_input), "Поле максимальной цены не отображается"

  @staticmethod
  def ads_prices_within_range(prices, min_value: int, max_value: int):
      assert prices, "Список цен пуст"
      for price in prices:
          assert min_value <= price <= max_value, f"Цена {price} не в диапазоне {min_value}-{max_value}"

  @staticmethod
  def ads_sorted_by_price_desc(prices):
      assert prices, "Список цен пуст"
      sorted_prices = sorted(prices, reverse=True)
      assert prices == sorted_prices, "Объявления не отсортированы по убыванию цены"

  @staticmethod
  def all_ads_have_same_category(categories):
      assert categories, "Список категорий пуст"
      first = categories[0]
      assert all(cat == first for cat in categories), "Не все объявления одной категории"

  @staticmethod
  def all_ads_urgent(flags):
      assert flags, "Список объявлений пуст"
      assert all(flags), "Не все объявления имеют метку 'Срочно'"

  @staticmethod
  def priority_filter_is_urgent(value: str):
      assert value == "Срочный", f"Фильтр 'Приоритет' равен {value}"

  @staticmethod
  def theme_changed(actual: str, expected: str):
      assert actual != expected, "Тема не изменилась"
