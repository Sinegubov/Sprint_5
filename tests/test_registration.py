from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegistrationLoc, AuthLoc
from helpers import Password
import data


class TestRegistration:

    def test_successful_registration_with_random_cred(self, wb):
        wb.get(data.URL.REG_PAGE)
        wb.find_element(*RegistrationLoc.name_input).send_keys(data.RandomCredential.NAME)
        wb.find_element(*RegistrationLoc.email_input).send_keys(data.RandomCredential.EMAIL)
        wb.find_element(*RegistrationLoc.password_input).send_keys(data.RandomCredential.PASSWORD)
        wb.find_element(*RegistrationLoc.reg_btn).click()
        WebDriverWait(wb, 10).until(expected_conditions.visibility_of_element_located(AuthLoc.login_btn))
        assert wb.current_url == data.URL.LOGIN_PAGE

    def test_failed_registration_wrong_password(self, wb):
        wb.get(data.URL.REG_PAGE)
        wb.find_element(*RegistrationLoc.name_input).send_keys(data.UserCredential.NAME)
        wb.find_element(*RegistrationLoc.email_input).send_keys(data.UserCredential.EMAIL)
        wb.find_element(*RegistrationLoc.password_input).send_keys(Password.bad_password())
        wb.find_element(*RegistrationLoc.reg_btn).click()

        WebDriverWait(wb, 3).until(expected_conditions.visibility_of_element_located
                                   (RegistrationLoc.error_invalid_password))

        assert wb.find_element(*RegistrationLoc.error_invalid_password).text == "Некорректный пароль"
