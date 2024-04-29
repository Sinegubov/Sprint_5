from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest

url = "https://stellarburgers.nomoreparties.site/register"


@pytest.mark.url(url)
def test_successful_registration(run_webdriver):
    driver = run_webdriver

    driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Pavel")
    driver.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys("sinegubov_8@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("123456")

    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()


@pytest.mark.url(url)
def test_failed_registration(run_webdriver):

    driver = run_webdriver

    driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Pavel")
    driver.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys("sinegubov_8@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("1")

    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((
        By.XPATH, "//p[@class='input__error text_type_main-default']")))

    status = driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']").text
    assert status == "Некорректный пароль"
