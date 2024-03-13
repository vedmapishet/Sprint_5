from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators

class TestDesigner:  #конструктор

    def test_transfer_to_sauces(self, driver):  #переход к разделу «Соусы»
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.span_sauces))

        driver.find_element(*locators.Locators.span_sauces).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(locators.Locators.current_span))

        assert driver.find_element(*locators.Locators.current_span).text == 'Соусы'

    def test_transfer_to_fillings(self, driver):  #переход к разделу «Начинки»
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.span_fillings))

        driver.find_element(*locators.Locators.span_fillings).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(locators.Locators.current_span))

        assert driver.find_element(*locators.Locators.current_span).text == 'Начинки'

    def test_transfer_to_buns(self, driver):  #переход к разделу «Булки»
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.span_sauces))

        driver.find_element(*locators.Locators.span_sauces).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.Locators.span_bungs))

        driver.find_element(*locators.Locators.span_bungs).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(locators.Locators.current_span))

        assert driver.find_element(*locators.Locators.current_span).text == 'Булки'