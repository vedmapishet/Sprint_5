from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators
import random


name = f'Тест'
email = f'123{random.randint(100, 999)}@yandex.ru'
password = f'{random.randint(100, 999)}abc'

incorrect_password = f'{random.randint(100, 999)}xx'


class TestRegistration:
    def test_registration_true(self, driver):  #успешная регистрация
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.personal_account))

        driver.find_element(*locators.Locators.personal_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.register_button))

        driver.find_element(*locators.Locators.register_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.button_registration))

        driver.find_element(*locators.Locators.input_name_field).send_keys(name)
        driver.find_element(*locators.Locators.input_email_field).send_keys(email)
        driver.find_element(*locators.Locators.input_password_field).send_keys(password)
        driver.find_element(*locators.Locators.button_registration).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.login_button))

        assert driver.find_element(*locators.Locators.login_button).text == 'Войти'

    def test_registration_incorrect_password(self, driver):  #ошибка для некорректного пароля
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.personal_account))

        driver.find_element(*locators.Locators.personal_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.register_button))

        driver.find_element(*locators.Locators.register_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.button_registration))

        driver.find_element(*locators.Locators.input_name_field).send_keys(name)
        driver.find_element(*locators.Locators.input_email_field).send_keys(email)
        driver.find_element(*locators.Locators.input_password_field).send_keys(incorrect_password)
        driver.find_element(*locators.Locators.button_registration).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.error_incorrect_password))

        assert driver.find_element(*locators.Locators.error_incorrect_password).text == 'Некорректный пароль'