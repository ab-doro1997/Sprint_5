import pytest
from locators.all_locators import LoginPageLocators, HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver")
class TestLogin:

    def test_login_via_main_button(self, driver):
        email = "aleksandra_doroshenko_22_1997@yandex.ru"
        password = "r*J!yf5b"
        wait = WebDriverWait(driver, 10)

        driver.get("https://stellarburgers.nomoreparties.site/")
        wait.until(EC.element_to_be_clickable(HomePageLocators.login_account_button)).click()
        wait.until(EC.visibility_of_element_located(LoginPageLocators.login_input)).send_keys(email)
        driver.find_element(*LoginPageLocators.password_input).send_keys(password)
        driver.find_element(*LoginPageLocators.login_button).click()
        assert driver.find_element(*HomePageLocators.account_link).is_displayed()

    def test_login_via_personal_account(self, driver):
        email = "aleksandra_doroshenko_22_1997@yandex.ru"
        password = "r*J!yf5b"
        wait = WebDriverWait(driver, 10)

        driver.get("https://stellarburgers.nomoreparties.site/")
        wait.until(EC.element_to_be_clickable(HomePageLocators.account_link)).click()
        wait.until(EC.visibility_of_element_located(LoginPageLocators.login_input)).send_keys(email)
        driver.find_element(*LoginPageLocators.password_input).send_keys(password)
        driver.find_element(*LoginPageLocators.login_button).click()
        assert wait.until(EC.visibility_of_element_located(HomePageLocators.account_link))

    def test_login_from_registration_form(self, driver):
        email = "aleksandra_doroshenko_22_1997@yandex.ru"
        password = "r*J!yf5b"
        wait = WebDriverWait(driver, 10)

        driver.get("https://stellarburgers.nomoreparties.site/register")
        wait.until(EC.element_to_be_clickable(LoginPageLocators.registration_link)).click()
        wait.until(EC.visibility_of_element_located(LoginPageLocators.login_input)).send_keys(email)
        driver.find_element(*LoginPageLocators.password_input).send_keys(password)
        driver.find_element(*LoginPageLocators.login_button).click()
        assert wait.until(EC.visibility_of_element_located(HomePageLocators.account_link))

    def test_login_from_password_recovery(self, driver):
        email = "aleksandra_doroshenko_22_1997@yandex.ru"
        password = "r*J!yf5b"
        wait = WebDriverWait(driver, 10)

        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        wait.until(EC.element_to_be_clickable(LoginPageLocators.back_to_login_link)).click()
        wait.until(EC.visibility_of_element_located(LoginPageLocators.login_input)).send_keys(email)
        driver.find_element(*LoginPageLocators.password_input).send_keys(password)
        driver.find_element(*LoginPageLocators.login_button).click()
        assert wait.until(EC.visibility_of_element_located(HomePageLocators.account_link))
