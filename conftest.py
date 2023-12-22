from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
