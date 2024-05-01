from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import AuthLoc, UserSpace, MainPageLoc


class TestTransferToConstructor:
    def test_successful_transfer_from_userspace_to_constructor_click_logo(self, wb, get_login_driver):
        wb.find_element(*AuthLoc.lk_btn).click()
        wb.find_element(*UserSpace.logo_btn).click()
        WebDriverWait(wb, 10).until(expected_conditions.visibility_of_element_located(UserSpace.logo_btn))
        assert wb.find_element(*MainPageLoc.h1_header).text == "Соберите бургер"

    def test_successful_transfer_from_userspace_to_constructor_click_constructor(self, wb, get_login_driver):
        wb.find_element(*AuthLoc.lk_btn).click()
        wb.find_element(*UserSpace.constructor_btn).click()
        WebDriverWait(wb, 10).until(expected_conditions.visibility_of_element_located(UserSpace.logo_btn))
        assert wb.find_element(*MainPageLoc.h1_header).text == "Соберите бургер"
