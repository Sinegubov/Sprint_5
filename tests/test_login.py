from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import AuthLoc, MainPageLoc, RegistrationLoc
import data


class TestLogin:

    @staticmethod
    def login(wb):
        wb.find_element(*AuthLoc.email_input).send_keys(data.UserCredential.EMAIL)
        wb.find_element(*AuthLoc.password_input).send_keys(data.UserCredential.PASSWORD)
        wb.find_element(*AuthLoc.login_btn).click()
        WebDriverWait(wb, 10).until(expected_conditions.visibility_of_element_located(MainPageLoc.order_button))

    def test_successful_login_main_page_button_log_in(self, wb):
        wb.get(data.URL.MAIN_PAGE)
        wb.find_element(*AuthLoc.login_main_btn).click()
        self.login(wb)
        order_btn = wb.find_element(*MainPageLoc.order_button).text
        assert wb.current_url == data.URL.MAIN_PAGE and (order_btn == 'Оформить заказ')

    def test_successful_login_button_personal_cabinet(self, wb):
        wb.get(data.URL.MAIN_PAGE)
        wb.find_element(*AuthLoc.lk_btn).click()
        self.login(wb)
        order_btn = wb.find_element(*MainPageLoc.order_button).text
        assert wb.current_url == data.URL.MAIN_PAGE and (order_btn == 'Оформить заказ')

    def test_successful_login_from_registration_form(self, wb):
        wb.get(data.URL.MAIN_PAGE)
        wb.find_element(*AuthLoc.lk_btn).click()
        wb.find_element(*AuthLoc.reg_btn).click()
        wb.find_element(*RegistrationLoc.login_btn).click()
        self.login(wb)
        order_btn = wb.find_element(*MainPageLoc.order_button).text
        assert wb.current_url == data.URL.MAIN_PAGE and (order_btn == 'Оформить заказ')

    def test_successful_login_from_password_recovery_form(self, wb):
        wb.get(data.URL.MAIN_PAGE)
        wb.find_element(*AuthLoc.lk_btn).click()
        wb.find_element(*AuthLoc.recovery_btn).click()
        wb.find_element(*RegistrationLoc.login_btn).click()
        self.login(wb)
        order_btn = wb.find_element(*MainPageLoc.order_button).text
        assert wb.current_url == data.URL.MAIN_PAGE and (order_btn == 'Оформить заказ')
