from selenium.webdriver.common.by import By


class Locators:

    personal_account = [By.XPATH, ".//a[@href='/account']"] # Личный кабинет

    register_button = [By.XPATH, ".//a[@href='/register']"] # Зарегистрироваться

    link_recover_password = [By.XPATH, ".//a[@href='/forgot-password']"]  # Восстановить пароль

    link_login = [By.XPATH, ".//a[@href='/login']"]  # Ссылка на Вход со страницы регистрации и восстановления пароля

    link_designer = [By.XPATH, ".//a[contains(@class, 'AppHeader_header__link')][@href='/']"]  # Ссылка на Конструктор

    link_logotip = [By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]/a"]  # Ссылка на конструктор из логотипа

    input_name_field = [By.XPATH, ".//label[text()='Имя']/following-sibling::input"] # Регистрация поле Имя

    input_email_field = [By.XPATH, ".//label[text()='Email']/following-sibling::input"] # Регистрация поле Email

    input_password_field = [By.XPATH, ".//input[@type='password']"] # Регистрация поле Пароль

    input_email_login = [By.XPATH, ".//label[text()='Email']/following-sibling::input"]  # Вход поле Email

    input_password_login = [By.XPATH, ".//label[text()='Пароль']/following-sibling::input"]  # Вход поле Пароль

    button_registration = [By.XPATH, ".//button[text()='Зарегистрироваться']"] # Кнопка Зарегистрироваться

    button_login_account = [By.XPATH, ".//button[contains(@class, 'button_button_size_large') and text()='Войти в аккаунт']"] # Кнопка Войти в аккаунт на главной

    login_button = [By.XPATH, ".//button[contains(@class, 'button_button_size_medium') and text()='Войти']"]  # кнопка Войти

    button_exit = [By.XPATH, ".//button[contains(@class, 'Account_button')][text()='Выход']"]  # Кнопка Выход из личного кабинета

    button_place_order = [By.XPATH, ".//button[contains(@class, 'button_button_size_large') and text()='Оформить заказ']"]  # Кнопка Оформить заказ на главной

    build_burger = [By.XPATH, ".//h1[text()='Соберите бургер']"]  # Надпись Соберите бургер

    error_incorrect_password = [By.XPATH, ".//p[contains(@class, 'input__error text') and text()='Некорректный пароль']"] # Надпись некорректный пароль при регистрации

    prof_personal_account = [By.XPATH, ".//a[@href='/account/profile' and text()='Профиль']"] # Профиль в Личном кабинете

    span_bungs = [By.XPATH, ".//span[text()='Булки']/parent::div"] # Булки

    span_sauces = [By.XPATH, ".//span[text()='Соусы']/parent::div"] # Соусы

    span_fillings = [By.XPATH, ".//span[text()='Начинки']/parent::div"] # Начинки

    current_span = [By.XPATH, ".//div[contains(@class, 'current')]/span"] # Текущий раздел