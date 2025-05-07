import pytest
from locators.all_locators import RegistrationPageLocators, LoginPageLocators
from helpers.data_helpers import DataGenerator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("driver")
class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        wait = WebDriverWait(driver, 10)

        name = DataGenerator.generate_name()
        email = DataGenerator.generate_login()
        password = DataGenerator.generate_password()

        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.name_input)).send_keys(name)
        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.email_input)).send_keys(email)
        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.password_input)).send_keys(password)
        wait.until(EC.element_to_be_clickable(RegistrationPageLocators.register_button)).click()

        assert wait.until(EC.visibility_of_element_located(LoginPageLocators.login_input)).is_displayed()


    def test_registration_with_invalid_password(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        wait = WebDriverWait(driver, 10)

        name = DataGenerator.generate_name()
        email = DataGenerator.generate_login()

        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.name_input)).send_keys(name)
        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.email_input)).send_keys(email)
        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.password_input)).send_keys("123")
        wait.until(EC.element_to_be_clickable(RegistrationPageLocators.register_button)).click()

        assert wait.until(EC.visibility_of_element_located(RegistrationPageLocators.password_error)).is_displayed()
