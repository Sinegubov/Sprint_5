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
    lk_btn = (By.XPATH, "//a[@href='/account']")  # Кнопка личного кабинета
    reg_btn = (By.XPATH, "//a[@class='Auth_link__1fOlj']")  # Кнопка Зарегистрироваться в личном кабинете
    recovery_btn = (By.XPATH, "(//a[@class='Auth_link__1fOlj'])[2]")  # Кнопка восстановления пароля
    recover_login_btn = (By.CLASS_NAME, "Auth_link__1fOlj")  # Кнопка Войти из формы восстановления пароля


class MainPageLoc:
    h1_header = (By.TAG_NAME, "h1")  # Заголовок h1 на главной странице "Соберите бургер"
    order_button = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка оформить заказ
    user_space = (By.XPATH, "//a[@href='/account']")  # Надпись "Личный кабинет"
    buns_construct_btn = (
        By.XPATH,
        "//section[@class='BurgerIngredients_ingredients__1N8v2']//div"
    )  # Раздел конструктора бургера "Булки" на главной странице
    buns_construct_text = (By.XPATH, "//h2[text()='Булки']")  # Заголовок каталога конструктора бургера "Булки"
    sauses_construct_btn = (
        By.XPATH,
        "//span[text()='Соусы']")  # Раздел конструктора бургера "Соусы" на главной странице
    sauses_construct_text = (
        By.XPATH, "//h2[text()='Соусы']"
    )  # Заголовок каталога конструктора бургера "Соусы"
    fillings_construct_btn = (
        By.XPATH, "//span[text()='Начинки']"
    )  # Раздел конструктора бургера "Начинки" на главной странице
    fillings_construct_text = (By.XPATH, "//h2[text()='Начинки']")  # Заголовок каталога конструктора бургера "Начинки"


class UserSpace:
    user_info = (
        By.XPATH, "//p[contains(@class,'Account_text__fZAIn text text_type_main-default')]"
    )  # Ссылка на профиль пользователя
    profile_email = (
        By.XPATH,
        "(//input[contains(@class,'text input__textfield')])[2]"
    )  # Поле c информацией о email пользователя
    logout_btn = (By.XPATH, ".//button[text()='Выход']")  # Кнопка выход
    logo_btn = (
        By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # Кнопка Логотип для перехода в конструктор
    constructor_btn = (
        By.XPATH, "//a[@class='AppHeader_header__link__3D_hX']")   # Кнопка Конструктор для перехода в конструктор
