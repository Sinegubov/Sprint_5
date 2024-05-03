from random import randint


class Password:
    @staticmethod
    def bad_password(pass_len=5):
        password = ""
        for i in range(int(pass_len)):
            password += f'{randint(0, 9)}'
        return password
