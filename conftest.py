from selenium import webdriver
from locators import AuthLoc
import pytest
import data


@pytest.fixture
def wb():
    wb = webdriver.Chrome()
    yield wb
    wb.quit()


@pytest.fixture
def get_login_driver(wb):
    wb.get(data.URL.LOGIN_PAGE)
    wb.find_element(*AuthLoc.email_input).send_keys(data.UserCredential.EMAIL)
    wb.find_element(*AuthLoc.password_input).send_keys(data.UserCredential.PASSWORD)
    wb.find_element(*AuthLoc.login_btn).click()
    return wb
