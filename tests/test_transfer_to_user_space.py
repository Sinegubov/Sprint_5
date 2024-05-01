from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import AuthLoc, UserSpace
import data


class TestTransferToUserSpace:
    def test_successful_transfer_from_main_page_to_userspace(self, wb, get_login_driver):
        wb.find_element(*AuthLoc.lk_btn).click()
        WebDriverWait(wb, 10).until(expected_conditions.visibility_of_element_located(UserSpace.user_info))
        assert wb.find_element(*UserSpace.profile_email).get_attribute("value") == data.UserCredential.EMAIL
