from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators

email = f'123@hh.ru'
password = f'N123456'


class TestAccountExit:

    def test_log_out_from_personal_account_using_exit_button(self, driver):  #выход по кнопке «Выйти» в личном кабинете
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.personal_account))

        driver.find_element(*locators.Locators.personal_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.login_button))

        driver.find_element(*locators.Locators.input_email_login).send_keys(email)
        driver.find_element(*locators.Locators.input_password_login).send_keys(password)
        driver.find_element(*locators.Locators.login_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.button_place_order))

        driver.find_element(*locators.Locators.personal_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.button_exit))

        driver.find_element(*locators.Locators.button_exit).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.login_button))

        assert '/login' in driver.current_url