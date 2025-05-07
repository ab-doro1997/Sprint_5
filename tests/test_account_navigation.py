import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.all_locators import HomePageLocators, AccountPageLocators, LoginPageLocators, ConstructorPageLocators

@pytest.mark.usefixtures("driver")
class TestAccountNavigation:

    def test_go_to_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        wait = WebDriverWait(driver, 10)
        email = "aleksandra_doroshenko_22_1997@yandex.ru"
        password = "r*J!yf5b"

        wait.until(EC.visibility_of_element_located(LoginPageLocators.login_input)).send_keys(email)
        wait.until(EC.visibility_of_element_located(LoginPageLocators.password_input)).send_keys(password)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.login_button)).click()
        wait.until(EC.element_to_be_clickable(HomePageLocators.account_link)).click()
        assert wait.until(EC.visibility_of_element_located(AccountPageLocators.logout_button))

    def test_go_from_account_to_constructor_from_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        wait = WebDriverWait(driver, 10)
        email = "aleksandra_doroshenko_22_1997@yandex.ru"
        password = "r*J!yf5b"

        wait.until(EC.visibility_of_element_located(LoginPageLocators.login_input)).send_keys(email)
        wait.until(EC.visibility_of_element_located(LoginPageLocators.password_input)).send_keys(password)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.login_button)).click()
        wait.until(EC.element_to_be_clickable(HomePageLocators.account_link)).click()
        wait.until(EC.element_to_be_clickable(HomePageLocators.constructor_link)).click()
        assert wait.until(EC.visibility_of_element_located(HomePageLocators.constructor_button))

    def test_go_to_constructor_from_logo(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        wait = WebDriverWait(driver, 10)
        email = "aleksandra_doroshenko_22_1997@yandex.ru"
        password = "r*J!yf5b"

        wait.until(EC.visibility_of_element_located(LoginPageLocators.login_input)).send_keys(email)
        wait.until(EC.visibility_of_element_located(LoginPageLocators.password_input)).send_keys(password)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.login_button)).click()
        wait.until(EC.element_to_be_clickable(HomePageLocators.account_link)).click()
        wait.until(EC.element_to_be_clickable(HomePageLocators.logo)).click()
        assert wait.until(EC.visibility_of_element_located(HomePageLocators.constructor_button))

    def test_logout(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        wait = WebDriverWait(driver, 10)
        email = "aleksandra_doroshenko_22_1997@yandex.ru"
        password = "r*J!yf5b"

        wait.until(EC.visibility_of_element_located(LoginPageLocators.login_input)).send_keys(email)
        wait.until(EC.visibility_of_element_located(LoginPageLocators.password_input)).send_keys(password)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.login_button)).click()
        wait.until(EC.element_to_be_clickable(HomePageLocators.account_link)).click()
        wait.until(EC.element_to_be_clickable(AccountPageLocators.logout_button)).click()
        assert wait.until(EC.visibility_of_element_located(LoginPageLocators.login_label))

    def test_constructor_sections(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        wait = WebDriverWait(driver, 10)
        email = "aleksandra_doroshenko_22_1997@yandex.ru"
        password = "r*J!yf5b"

        wait.until(EC.visibility_of_element_located(LoginPageLocators.login_input)).send_keys(email)
        wait.until(EC.visibility_of_element_located(LoginPageLocators.password_input)).send_keys(password)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.login_button)).click()

        wait.until(EC.element_to_be_clickable(ConstructorPageLocators.sauces_tab)).click()
        assert wait.until(EC.visibility_of_element_located(ConstructorPageLocators.sauces_section))


        wait.until(EC.element_to_be_clickable(ConstructorPageLocators.fillings_tab)).click()
        assert wait.until(EC.visibility_of_element_located(ConstructorPageLocators.fillings_section))


        wait.until(EC.element_to_be_clickable(ConstructorPageLocators.buns_tab)).click()
        assert wait.until(EC.visibility_of_element_located(ConstructorPageLocators.buns_section))


