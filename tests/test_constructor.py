from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPageLoc
import data


class TestConstructor:
    def test_constructor_open_buns(self, wb, get_login_driver):
        wb.get(data.URL.MAIN_PAGE)
        wb.find_element(*MainPageLoc.buns_construct_btn).click()
        WebDriverWait(wb, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLoc.buns_construct_text))
        assert wb.find_element(*MainPageLoc.buns_construct_text).text == "Булки"

    def test_constructor_open_sauses(self, wb, get_login_driver):
        wb.get(data.URL.MAIN_PAGE)
        wb.find_element(*MainPageLoc.sauses_construct_btn).click()
        WebDriverWait(wb, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLoc.sauses_construct_text))
        assert wb.find_element(*MainPageLoc.sauses_construct_text).text == "Соусы"

    def test_constructor_open_fillings(self, wb, get_login_driver):
        wb.get(data.URL.MAIN_PAGE)
        wb.find_element(*MainPageLoc.fillings_construct_btn).click()
        WebDriverWait(wb, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLoc.fillings_construct_text))
        assert wb.find_element(*MainPageLoc.fillings_construct_text).text == "Начинки"
