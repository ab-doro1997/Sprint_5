from selenium.webdriver.common.by import By

class HomePageLocators:
    login_account_button = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка войти в аккаунт
    account_link = (By.XPATH, "//p[text()='Личный Кабинет']") # Ссылка на страницу личного кабинета
    logo = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # Логотип Stellar Burgers
    constructor_button = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка «Конструктор»
    constructor_link = (By.XPATH, "//p[text()='Конструктор']")  # Ссылка на страницу конструктора

class RegistrationPageLocators:
    name_input = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input") # Поле ввода для имени
    email_input = (By.XPATH, "//label[text() = 'Email']/following-sibling::input") # Поле ввода для Email
    password_input = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input") # Поле ввода для пароля
    register_button = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка «Зарегистрироваться»
    password_error = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]") # Сообщение об ошибке под полем пароля при некорректном вводе

class LoginPageLocators:
    login_label = (By.XPATH, "//h2[text() = 'Вход']") # Заголовок страницы «Вход»
    login_input = (By.XPATH, "//label[text() = 'Email']/following-sibling::input") # Поле ввода для Email
    password_input = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input") # Поле ввода для пароля
    login_button = (By.XPATH, "//button[text() = 'Войти']") # Кнопка «Войти»
    registration_link = (By.XPATH, "//a[@href = '/login']") # Ссылка на страницу регистрации
    restore_password_link = (By.XPATH, "//a[@href ='/forgot-password']") # Ссылка на восстановление пароля
    back_to_login_link = (By.XPATH, "//a[@href='/login']") # Локатор ссылки «Войти» на странице восстановления пароля

class AccountPageLocators:
    name_input = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input") # Поле ввода для имени (в личном кабинете)
    login_input = (By.XPATH, "//label[text() = 'Логин']/following-sibling::input") # Поле ввода для логина
    password_input = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input") # Поле ввода для пароля
    logout_button = (By.XPATH, "//button[text()='Выход']") # Кнопка «Выход»

class ConstructorPageLocators:
    buns_tab = (By.XPATH, "//span[text()='Булки']")  # Вкладка «Булки»
    sauces_tab = (By.XPATH, "//span[text()='Соусы']")  # Вкладка «Соусы»
    fillings_tab = (By.XPATH, "//span[text()='Начинки']")  # Вкладка «Начинки»
    buns_section = (By.XPATH, "//h2[text()='Булки']")  # Заголовок раздела «Булки»
    sauces_section = (By.XPATH, "//h2[text()='Соусы']")  # Заголовок раздела «Соусы»
    fillings_section = (By.XPATH, "//h2[text()='Начинки']")  # Заголовок раздела «Начинки»
    constructor_title = (By.XPATH, "//h1[text()='Соберите бургер']")  # Заголовок конструктора
