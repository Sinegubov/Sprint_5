from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import UserSpace, AuthLoc
import data


class TestLogout:
    def test_successful_logout(self, wb, get_login_driver):
        wb.find_element(*AuthLoc.lk_btn).click()
        WebDriverWait(wb, 10).until(expected_conditions.visibility_of_element_located(UserSpace.user_info))
        wb.find_element(*UserSpace.logout_btn).click()
        WebDriverWait(wb, 10).until(expected_conditions.visibility_of_element_located(AuthLoc.login_btn))
        assert wb.current_url == data.URL.LOGIN_PAGE
        assert wb.find_element(*AuthLoc.login_btn).text == "Войти"
