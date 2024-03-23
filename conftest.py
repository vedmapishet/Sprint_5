import pytest
from selenium import webdriver


@pytest.fixture
# подключаем драйвер
def driver():
    driver = webdriver.Chrome()  # создали драйвер
    driver.maximize_window()  # полноэкранный режим
    driver.get('https://stellarburgers.nomoreparties.site/')  # открыли страницу
    yield driver

    driver.quit() #закрыть браузер

