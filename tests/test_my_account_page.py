import allure

from data.urls import Urls, Endpoints
from pages.login_page import LoginPage
from pages.main_page import HeaderPage
from pages.my_account_page import MyAccountPage


class TestMyAccountPage:
    @allure.title('Проверка перехода в "Личный кабинет"')
    @allure.description('''
                        1. Создаем пользователя через API
                        2. Переход на страницу сервиса
                        2. Логин в систему
                        3. Клик по кнопке "Личный кабинет"
                        4. Проверяем отображение формы "Личный кабинет"
                        5. Удаляем пользователя через API
                        ''')
    def test_redirect_to_my_account_page(self, driver, create_new_user, login):
        header = HeaderPage(driver)
        my_account = MyAccountPage(driver)
        header.click_on_my_account_button()
        assert my_account.check_profile_area_form_visible() and my_account.get_current_url() == (
                Urls.MAIN_URL + Endpoints.MY_ACCOUNT)

    @allure.title('Проверка перехода в "История Заказов"')
    @allure.description('''
                        1. Создаем пользователя через API
                        2. Переход на страницу сервиса
                        3. Логин в систему
                        4. Клик по кнопке "Личный кабинет"
                        5. Клик по кноке "История заказов"
                        6. Провеям отображение формы "История заказов"
                        7. Удаляем пользователя через API
                        ''')
    def test_redirect_to_orders_history(self, driver, create_new_user, login):
        header = HeaderPage(driver)
        my_account = MyAccountPage(driver)
        header.click_on_my_account_button()
        my_account.click_on_orders_history_button()
        assert my_account.check_profile_area_form_visible() and my_account.get_current_url() == (
                Urls.MAIN_URL + Endpoints.ORDER_HISTORY)

    @allure.title('Проверка выхода из аккаунта"')
    @allure.description('''
                        1. Создаем пользователя через API
                        2. Переход на страницу сервиса
                        3. Логин в систему
                        4. Клик по кнопке "Личный кабинет"
                        5. Клик по кноке "Выход"
                        6. Проверяем выход из аккаунта
                        7. Удаляем пользователя через API
                        ''')
    def test_logout(self, driver, create_new_user, login):
        header = HeaderPage(driver)
        my_account = MyAccountPage(driver)
        login_page = LoginPage(driver)
        header.click_on_my_account_button()
        my_account.click_on_logout_button()
        assert login_page.check_authorization_form_verification() and login_page.get_current_url() == (
                Urls.MAIN_URL + Endpoints.LOGIN)
