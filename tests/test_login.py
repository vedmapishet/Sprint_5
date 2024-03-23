from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators


email = f'123@hh.ru'
password = f'N123456'

class TestLogin:

    def test_login_on_main_page(self, driver):  #вход по кнопке «Войти в аккаунт» на главной
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.button_login_account))

        driver.find_element(*locators.Locators.button_login_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.login_button))

        driver.find_element(*locators.Locators.input_email_login).send_keys(email)
        driver.find_element(*locators.Locators.input_password_login).send_keys(password)
        driver.find_element(*locators.Locators.login_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.button_place_order))

        assert driver.find_element(*locators.Locators.button_place_order).text == 'Оформить заказ'

    def test_login_in_personal_account(self, driver):  #вход через кнопку «Личный кабинет»
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.personal_account))

        driver.find_element(*locators.Locators.personal_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.login_button))

        driver.find_element(*locators.Locators.input_email_login).send_keys(email)
        driver.find_element(*locators.Locators.input_password_login).send_keys(password)
        driver.find_element(*locators.Locators.login_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.button_place_order))

        assert driver.find_element(*locators.Locators.button_place_order).text == 'Оформить заказ'

    def test_login_on_registration_form(self, driver):  #вход через кнопку в форме регистрации

        driver.find_element(*locators.Locators.personal_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.register_button))

        driver.find_element(*locators.Locators.register_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.link_login))

        driver.find_element(*locators.Locators.link_login).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.login_button))

        driver.find_element(*locators.Locators.input_email_login).send_keys(email)
        driver.find_element(*locators.Locators.input_password_login).send_keys(password)
        driver.find_element(*locators.Locators.login_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.button_place_order))

        assert driver.find_element(*locators.Locators.button_place_order).text == 'Оформить заказ'

    def test_login_on_password_recover_form(self, driver):  #вход через кнопку в форме восстановления пароля
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.personal_account))

        driver.find_element(*locators.Locators.personal_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.link_recover_password))

        driver.find_element(*locators.Locators.link_recover_password).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.link_login))

        driver.find_element(*locators.Locators.link_login).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.login_button))

        driver.find_element(*locators.Locators.input_email_login).send_keys(email)
        driver.find_element(*locators.Locators.input_password_login).send_keys(password)
        driver.find_element(*locators.Locators.login_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.button_place_order))

        assert driver.find_element(*locators.Locators.button_place_order).text == 'Оформить заказ'