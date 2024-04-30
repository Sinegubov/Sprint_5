from selenium.webdriver.common.by import By


class RegistrationLoc:
    name_input = (By.XPATH, "//input[@name='name']")  # Поле ввода имени
    email_input = (By.XPATH, "(//input[@name='name'])[2]")  # Поле ввода email
    password_input = (By.XPATH, "//input[@name='Пароль']")  # Поле ввода пароля
    reg_btn = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    error_invalid_password = (By.XPATH, ".//p[text() = 'Некорректный пароль']")  # Ошибка при вводе некорректного пароля
    login_btn = (By.CLASS_NAME, "Auth_link__1fOlj")  # Кнопка войти в форме регистрации


class AuthLoc:
    auth_form = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']")  # Форма авторизации
    email_input = (By.NAME, "name")  # Поле ввода email
    password_input = (By.NAME, "Пароль")  # Поле ввода пароля
    login_btn = (By.XPATH, "//button[text()='Войти']")  # Кнопка войти
    login_main_btn = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка войти в аккаунт на главной странице
    lk_btn = (By.XPATH, "// p[text() = 'Личный Кабинет']")  # Кнопка личного кабинета
    reg_btn = (By.XPATH, "//a[@class='Auth_link__1fOlj']")  # Кнопка Зарегистрироваться в личном кабинете
    recovery_btn = (By.XPATH, "(//a[@class='Auth_link__1fOlj'])[2]")  # Кнопка восстановления пароля
    recover_login_btn = (By.CLASS_NAME, "Auth_link__1fOlj")  # Кнопка Войти из формы восстановления пароля


class MainPageLoc:
    h1_header = (By.TAG_NAME, "h1")  # Заголовок h1 на главной странице "Соберите бургер"
    order_button = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка оформить заказ
