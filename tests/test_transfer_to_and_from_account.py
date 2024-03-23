from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators


email = f'123@hh.ru'
password = f'N123456'


class TestTransferToAndFromAccount:
    def test_transfer_to_personal_account(self, driver):  # переход по клику на «Личный кабинет»
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.personal_account))

        driver.find_element(*locators.Locators.personal_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.login_button))

        driver.find_element(*locators.Locators.input_email_login).send_keys(email)
        driver.find_element(*locators.Locators.input_password_login).send_keys(password)
        driver.find_element(*locators.Locators.login_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.button_place_order))

        driver.find_element(*locators.Locators.personal_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.prof_personal_account))

        assert '/account/profile' in driver.current_url

    def test_transfer_to_designer_from_personal_account(self, driver):  #переход по клику на «Конструктор»
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.personal_account))

        driver.find_element(*locators.Locators.personal_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.login_button))

        driver.find_element(*locators.Locators.input_email_login).send_keys(email)
        driver.find_element(*locators.Locators.input_password_login).send_keys(password)
        driver.find_element(*locators.Locators.login_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.button_place_order))

        driver.find_element(*locators.Locators.personal_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.prof_personal_account))

        driver.find_element(*locators.Locators.link_designer).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.build_burger))

        assert driver.find_element(*locators.Locators.build_burger).text == 'Соберите бургер' and driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_transfer_to_logotip_from_personal_account(self, driver):  #переход по клику на логотип Stellar Burgers
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.personal_account))

        driver.find_element(*locators.Locators.personal_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.login_button))

        driver.find_element(*locators.Locators.input_email_login).send_keys(email)
        driver.find_element(*locators.Locators.input_password_login).send_keys(password)
        driver.find_element(*locators.Locators.login_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.button_place_order))

        driver.find_element(*locators.Locators.personal_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.prof_personal_account))

        driver.find_element(*locators.Locators.link_logotip).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.build_burger))

        assert driver.find_element(*locators.Locators.build_burger).text == 'Соберите бургер' and driver.current_url == 'https://stellarburgers.nomoreparties.site/'