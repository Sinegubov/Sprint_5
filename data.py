from random import randint


class URL:
    MAIN_PAGE = "https://stellarburgers.nomoreparties.site/"
    REG_PAGE = f"{MAIN_PAGE}register"
    LOGIN_PAGE = f"{MAIN_PAGE}login"
    PERSONAL_CABINET_PAGE = f"{MAIN_PAGE}account/profile"


class UserCredential:
    NAME = "Pavel Sinegubov"
    EMAIL = "pavelsinegubov8123@gmail.com"
    PASSWORD = "123456"

    @staticmethod
    def bad_password(pass_len=5):
        password = ""
        for i in range(int(pass_len)):
            password += f'{randint(0, 9)}'
        return password


class RandomCredential:
    NAME = 'Новый пользователь'
    EMAIL = f'user{randint(0, 999)}_QWE@yandex.ru'
    PASSWORD = f'{randint(1000, 9999)}xyz'
