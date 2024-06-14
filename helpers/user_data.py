import allure
from faker import Faker


class Person:
    @staticmethod
    @allure.step('Генерация email, password, name пользователя')
    def create_data_correct_user():
        faker = Faker('ru_RU')
        data = {
            "email": faker.email(),
            "password": faker.password(),
            "name": faker.first_name()
        }
        return data
