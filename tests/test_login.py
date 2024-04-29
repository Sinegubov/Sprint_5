from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest

url = "https://stellarburgers.nomoreparties.site/login"


@pytest.mark.url(url)
def test_successful_login(run_webdriver):
    driver = run_webdriver

    driver.find_element(By.NAME, "name").send_keys("pavelsinegubov8123@gmail.com")
    driver.find_element(By.NAME, "Пароль").send_keys("123456")

    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((
        By.TAG_NAME, "h1")))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"