from selenium import webdriver
import pytest

@pytest.fixture(scope='function')
def wb():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
