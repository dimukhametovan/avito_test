import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver(is_mobile: bool):
    options = Options()
    if is_mobile:
        mobile_emulation = {"deviceName": "iPhone SE"}
        options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver


@pytest.fixture(scope="session")
def base_url():
    return "https://cerulean-praline-8e5aa6.netlify.app"


@pytest.fixture
def desktop_driver():
    driver = create_driver(is_mobile=False)
    yield driver
    driver.quit()


@pytest.fixture
def mobile_driver():
    driver = create_driver(is_mobile=True)
    yield driver
    driver.quit()
