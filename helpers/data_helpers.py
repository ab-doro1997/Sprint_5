import random
import string

class DataGenerator:
    @staticmethod
    def generate_name() -> str:
        name_lenght = random.randint(2, 10)
        name = ''.join(
            random.choice(string.ascii_letters + string.digits)
            for _ in range(name_lenght)
        )

        return name

    @staticmethod
    def generate_login() -> str:
        login_lenght = random.randint(3, 12)
        login = ''.join(random.choice(string.ascii_letters + string.digits)
            for _ in range(login_lenght)
        )

        domains = ["ya.ru", "yandex.ru", "gmail.com", "mail.ru"]
        domain = random.choice(domains)

        return f'{login}@{domain}'.lower()

    @staticmethod
    def generate_password(min_lenght=6, max_lenght=14) -> str:
        lenght = random.randint(min_lenght, max_lenght)
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(lenght))

        return password

